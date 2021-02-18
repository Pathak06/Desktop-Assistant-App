import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import pyjokes
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',140)
engine.setProperty('volume',1.5)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = (datetime.datetime.now().hour)
    if(hour>=6 and hour<12):
        engine.say('Good Morning!!')
    elif(hour>=12 and hour<18):
        engine.say('Good Afternoon!!')
    else:
        engine.say('Good Evening!!')
    engine.say('Hello Sir!! I am Jarvis. I am your personal voice assistant. Tell me what you want me to do? ')
    engine.runAndWait()



def command():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1



        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print('User said:- ',query)
    except Exception as e:
        print('Can you say it again?')

        return 'exit'

    return query

if __name__ == '__main__':

    wish()



    while True:

        inp = command().lower()
        if('wikipedia' in inp):
            speak('Searching Wikipedia...')
            inp = inp.replace('wikipedia','')
            result = wikipedia.summary(inp,sentences=2)
            speak('According to Wikipedia...')
            speak(result)

        elif('youtube' in inp):
            webbrowser.open('youtube.com')

        elif ('google' in inp):
            webbrowser.open('google.com')

        elif('play' in inp):
            song = inp.replace('play','')
            speak('Playing ' + song)
            pywhatkit.playonyt(song)



        elif('open linkedin' in inp):
            webbrowser.open('linkedin.com')
        elif('joke' in inp):
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif ('play music' in inp):
            music_dir = 'C:\\Users\\HP\\Music\\Playlists'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in inp:
            t = datetime.datetime.now().strftime('%H:%M:%S')
            speak('The time is:- ' + t)

        elif 'send a message' in inp:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Please say the message...')
                audio = r.listen(source)
                txt = r.recognize_google(audio,language='en-in')
                pywhatkit.sendwhatmsg('+919624837007',txt,14,46)



        elif('exit' in inp):
            exit()

        elif ('how' or 'what' or 'when' or 'why' or 'if' or 'which' or 'whom' in inp):
            ans = inp
            speak('Finding answer to ' + ans)
            pywhatkit.search(ans)
