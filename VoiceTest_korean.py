import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    for i in range(1):
        print(">>>", end=" ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="ko-KR")
            print(text)

        except:
            pass
