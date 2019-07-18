import speech_recognition as sr
import pyttsx3

import webbrowser
import pygame
import os
import time


r = sr.Recognizer()
engine = pyttsx3.init()


def do(speaker_text, text_to_print, text_to_say, web_url):
    if web_url == 0:
        if text == speaker_text:
            print(text_to_print + "\n")
            if text_to_say == 0:
                engine.say(text_to_print)
            else:
                engine.say(text_to_say)
            engine.runAndWait()
    else:
        if text == speaker_text:
            print(text_to_print + "\n")
            if text_to_say == 0:
                engine.say(text_to_print)
            else:
                engine.say(text_to_say)

            engine.runAndWait()
            webbrowser.open(web_url)


with sr.Microphone() as source:

    for i in range(1):
        print("무엇을 도와드릴까요?\n>>>", end=" ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="ko-KR")
            print(text)

            # 명령들
            do("유튜브 열어 줘", "유튜브 여는 중...", "알겠습니다. 유튜브 여는 중.", "https://www.youtube.com")
            do("안녕", "안녕하세요!", 0, 0)
            do("안녕하세요", "안녕하세요", "안녕하십니까!", 0)


        except:
            print("\n인식에 실패하였습니다. 다시 시도해 주세요.")
            engine.say("인식에 실패하였습니다. 다시 시도해 주세요.")
            engine.runAndWait()
