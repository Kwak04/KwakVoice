import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    for i in range(1):
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="ko-KR")
            print(text)

        except:
            print("인식 실패")
