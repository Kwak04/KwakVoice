import speech_recognition as sr
import pyttsx3

import webbrowser


r = sr.Recognizer()
engine = pyttsx3.init()


def do(speaker_text, text_to_print, text_to_say, speaker_text_to_print, web_url):
    # 함수 인수 도움말
    # speaker_text: 마이크로 인식되는 사용자의 텍스트
    # text_to_print: KwakVoice가 콘솔에 출력할 메시지
    # text_to_say: KwakVoice가 tts로 말할 메시지 (text_to_print와 같은 경우 0 입력)
    # speaker_text_to_print: 사용자의 텍스트를 인식되는 것과 다르게 표시하고 싶은 경우 텍스트 입력 (speaker_text와 같으면 0 입력)
    # web_url: 웹사이트를 표시하고 싶은 경우 url 입력 (웹사이트를 표시하지 않아도 되는 경우 0 입력)

    if web_url == 0:
        if text == speaker_text:
            if speaker_text_to_print == 0:
                print(text)
            else:
                print(speaker_text_to_print)
            print(text_to_print + "\n")
            if text_to_say == 0:
                engine.say(text_to_print)
            else:
                engine.say(text_to_say)

            engine.runAndWait()
    else:
        if text == speaker_text:
            if speaker_text_to_print == 0:
                print(text)
            else:
                print(speaker_text_to_print)
            print(text_to_print + "\n")
            if text_to_say == 0:
                engine.say(text_to_print)
            else:
                engine.say(text_to_say)

            engine.runAndWait()
            webbrowser.open(web_url)


with sr.Microphone() as source:

    while True:
        print("무엇을 도와드릴까요?\n>>>", end=" ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="ko-KR")

            # 명령들

            # # 대화
            do("안녕", "안녕하세요!", 0, 0, 0)
            do("안녕하세요", "안녕하세요", "안녕하십니까!", 0, 0)

            # # 웹사이트 열기
            do("유튜브 열어 줘", "유튜브 여는 중...", "알겠습니다. 유튜브 여는 중.", "유튜브 열어줘", "https://www.youtube.com")

            # # 기타
            do("최연욱 바보", "ㅇㅈ합니다.", "인정합니다. 최연욱 병신.", "최연욱 바보똥멍청이쌉병신", 0)

        except:  # 인식에 실패하였을 경우 예외 처리
            print("\n인식에 실패하였습니다. 다시 시도해 주세요.")
            engine.say("인식에 실패하였습니다. 다시 시도해 주세요.")
            engine.runAndWait()
