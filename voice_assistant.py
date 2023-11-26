import speech_recognition as sr
import webbrowser

END_KEYWORD = "stop conversation"
SEARCH_KEYWORD = "search"

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def main():
    # obtain audio from the microphone
    r = sr.Recognizer()

    while True:
        with sr.Microphone(device_index=1) as source:
            print("Say something!")
            audio = r.listen(source, timeout=3)

        # recognize speech using Sphinx
        text = ""
        try:
            text = r.recognize_sphinx(audio)
            print("You said", text)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        if END_KEYWORD in text.lower():
            break

        if SEARCH_KEYWORD in text.lower():
            index = text.rfind(SEARCH_KEYWORD) + len(SEARCH_KEYWORD)
            search = text[index:].replace(" ", "+")
            webbrowser.open_new(url=f"google.com/search?q={search}")


if __name__ == "__main__":
    main()
