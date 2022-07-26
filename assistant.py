import spacy
import pyttsx3
from sympy import re
import miscellaneous.Terminal

import speech_recognition as sr

class Assistant:
  
  def __init__(self):
    self.nlp = spacy.load("en_core_web_lg")
    self.terminal = miscellaneous.Terminal()
    self.voice_engine = pyttsx3.init()
    self.recognizer = sr.Recognizer()
  
  def say(self, message) -> None:
    self.voice_engine.say(message);
      
  def listen(self) -> None:
    try:
      with sr.Microphone() as microphone:
        # Set the ambient noise to increase the range of recongizing the audio.
        self.recognizer.adjust_for_ambient_noise(microphone, 0.5)
        audio = self.recognizer.listen(microphone)
        
      return self.recognizer.recognize_google(audio, "en-us")
    except sr.WaitTimeoutError:
      print("Since you didn't say anything, I'll just listen again and again and say this again and again too.")
      pass
    except sr.UnknownValueError:
      self.say("I didn't understand what you just said.")
      pass
    
  def execute_voice_command(self, voice_message) -> None:
    with open("./config/voice_commands.json", "r") as voice_commands:
      pass
