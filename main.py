import speech_recognition as sr
from gtts import gTTS
import pyttsx3
  
chat_context = []

def listen():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
  try:
    user_input = r.recognize_google(audio)
    print("You said:", user_input)
    return user_input
  except sr.UnknownValueError:
    print("Could not understand audio")
    return None
  except sr.RequestError as e:
    print("Request failed; {0}".format(e))
    return None

def speak(text):
  engine.say(text)
  engine.runAndWait()

while True:
  engine = pyttsx3.init()
  user_input = listen()
  
  if user_input:
    # could query with gemini and then speak back the response here 
    speak(user_input)

  else:
    speak("Sorry, I didn't catch that.")
  print("-" * 20)


# query with gemini, get the response, and speak it back
# keep chat context, so that gemini can provide more accurate response based on previous messages