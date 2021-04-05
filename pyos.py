import pyttsx3
import os
import pyaudio
import speech_recognition as sr

pyttsx3.speak("Welcome to my tools \n \n...")

r=sr.Recognizer()
with sr.Microphone() as source:
    print('start saying !!')
    audio = r.listen(source)
    print('We got it !!')

data=r.recognize_google(audio)
print(data)
if ("date" in data) and (("run" in data) or ("execute" in data)):
    os.system("date")
elif("chrome" in data) or ("Chrome" in data):
    os.system("start chrome")
elif("firefox" in data) or ("Firefox" in data):
    os.system("start firefox")
elif("notepad" in data) or ("Notepad" in data ):
    os.system("notepad")
elif(("Windows Media Player" in data) or("wmplayer" in data)):
    os.system("start wmplayer")
else:
    print("command not found")
