import speech_recognition as sr
import webbrowser
import os
import time
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    while True:
        print("What can I help you with?")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)

            if text == "hello":
                print(text)
                print("OK")
                engine.say("안녕하세요.")
                engine.runAndWait()

        except:
            print("오류입니다.")

            engine.say("오류입니다.")