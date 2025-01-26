import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak('I am Jarvis maam. Please tell me how may I help you')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        speak('Say that again please...')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sanjeevanishivde87@gmail.com', 'your-password')
    server.sendmail('sanjeevanishivde87@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', 'What is Ai in wikipedia.')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open notepad' in query:
            npath = 'C:\WINDOWS\system32\\notepad.exe'
            os.startfile(npath)


        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Sanjivani\\Music\\My Music\\Musics'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'maam, the time is {strTime}')

        elif 'open code' in query:
            codePath = 'C:\\Users\\Sanjivani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

            # to close any application
        elif "close notepad" in query:
            speak("okay Maam, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close code" in query:
            speak("okay Maam, closing VS Code")
            os.system("taskkill /f /im code.exe")

        elif 'no thank you' in query:
            speak('thanks for using me maam, Have a Good Day.')
            sys.exit()


        elif 'email to sanjeevani' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'sanjeevanishivde87@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry my friend sanjeevani. I am not able to send this email')


        speak('maam,do you have any other work?')
