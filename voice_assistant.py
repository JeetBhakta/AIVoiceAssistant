import speech_recognition as sr
import webbrowser
import os
import re

MICROPHONE = 2
END_KEYWORD = "stop conversation"
SEARCH_KEYWORD = "search"
WEATHER_KEYWORD = "weather"
NEWS_KEYWORD = "news"
TIMER_KEYWORD = "timer"
NOTES_KEYWORD = "right"


def voice_assistant():
    """
    Voice AI assistant using speech recognition that can do a few simple tasks.
    1. Search phrase on Google
    2. Check the weather
    3. Check news
    4. Take notes
    """
    # obtain audio from the microphone
    r = sr.Recognizer()

    while True:
        # Dylan index: 1
        # Jeet index: 2
        with sr.Microphone(device_index=MICROPHONE) as source:
            print("Say something!")
            audio = r.listen(source, timeout=10)

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
        elif SEARCH_KEYWORD in text.lower():
            index = text.rfind(SEARCH_KEYWORD) + len(SEARCH_KEYWORD) + 1
            search = text[index:].replace(" ", "+")
            webbrowser.open_new(url=f"google.com/search?q={search}")
        elif WEATHER_KEYWORD in text.lower():
            webbrowser.open_new(url="weather.com/weather/today")
        elif NEWS_KEYWORD in text.lower():
            webbrowser.open_new(url="nbcnews.com")
        elif TIMER_KEYWORD in text.lower():
            pass
            # minutes = 1
            # seconds = 0
            # matches = re.findall(r'(\d+)\s*(minute|second)s?', text.lower())
            # if "minutes" in text.lower():
            #     minutes = sum(int(value) for value, unit in matches if unit == "minutes")
            # if "seconds" in text.lower():
            #     seconds = sum(int(value) for value, unit in matches if unit == "seconds")
            # webbrowser.open_new(url=f"https://www.timerminutes.com/{minutes}-minutes-{seconds}-seconds-timer/")
        elif NOTES_KEYWORD in text.lower():
            note_file = "note.txt"
            with open(note_file, "a") as file:
                os.startfile(note_file)
                file.write(text[(text.index("right") + len(NOTES_KEYWORD) + 1):] + "\n")


if __name__ == "__main__":
    voice_assistant()
