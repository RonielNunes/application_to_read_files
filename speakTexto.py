import pyttsx3
from pyttsx3 import engine

def speak(text) -> None:
    engine = pyttsx3.init() #criação de objeto
    engine.setProperty('rate', 230)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait ()
