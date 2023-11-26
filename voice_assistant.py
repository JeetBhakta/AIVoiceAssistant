import speech_recognition as sr
import webbrowser

def ttsThings():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        end_phrase = "Break conversation"
        search_keyword = "search"
        while True:
            try:
                print("Start:")
                audio_data = recognizer.listen(source, timeout=3)
                print("END")

                text = recognizer.recognize_sphinx(audio_data)
                print("You said:", text)

                if end_phrase.lower() in text.lower():
                    print("Ending Coversation!!!")
                    break

                if search_keyword in text.lower():
                    webbrowser.open_new(url="https://www.google.com/search?q=" + str(text[text.index(search_keyword):]))

            except sr.UnknownValueError:
                print("Could not understand audio")

            except sr.RequestError as e:
                print(f"Error connecting to Google Speech Recognition service; {e}")

if __name__ == "__main__":
    ttsThings()
