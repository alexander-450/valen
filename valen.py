import speech_recognition as sr
import time
import wikipedia
import datetime
import pyjokes
from time import ctime
import webbrowser
from playsound import playsound
import os
import random
from gtts import gTTS
import pywhatkit


def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        alexis_speak('Good Morning Alexander !')
    elif hour >= 12 and hour < 18:
        alexis_speak("Good Afternoon Alexander !")
    else:
        alexis_speak("Good Evening Alexander !")
    alexis_speak('I am your Assistant Alice')
    alexis_speak('How may i help you')


r = sr.Recognizer()


def listen(ask=False):
    # source as my microphone
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        # audio contains what i say
        audio = r.listen(source)
        voice_data = ''
        try:
            # voice_data converts what i say to a string
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('Sorry, i did not get you Alexander')
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down. Connect to the Internet')
        return voice_data


def respond_listen(voice_data2):
    if 'what is your name' in voice_data2:
        alexis_speak('You already know Alex')
        alexis_speak('I am Alice you made')
    if 'Hello Alice' in voice_data2:
        alexis_speak('Hello Alex')
    if 'good morning' in voice_data2:
        alexis_speak("A warm" + voice_data2)
        alexis_speak("How are you Mister")
    if 'how are you' in voice_data2 or 'how are you doing' in voice_data2:
        alexis_speak('I am fine, Thank you')
        alexis_speak('what about you, sir')
    if 'fine' in voice_data2 or 'i am fine' in voice_data2 or 'doing good' in voice_data2 or 'i am okay' in voice_data2:
        alexis_speak('it\'s good to know that you are fine')
        alexis_speak('so what are your plans for today')
    if 'fine what about you' in voice_data2 or 'i am fine what about you' in voice_data2 \
            or 'doing great what about you' in voice_data2 or 'i am okay' in voice_data2 \
            or 'doing good what about you' in voice_data2:
        alexis_speak('it\'s good to know that you are fine')
        alexis_speak('so what are your plans for today')
    if 'stop listening' in voice_data2 or "don't listening" in voice_data2:
        alexis_speak('Going off for a while, wake me up anytime.')
        exit()
    if 'find location' in voice_data2:
        location = listen('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('here is what i found for you\n' + location)
    if 'search for' in voice_data2:
        search = listen('what should i search for you')
        url = 'https://google.com/search?q=' + search
        alexis_speak('here is what i found for you ' + search)
        time.sleep(2)
        webbrowser.get().open(url)
    if 'what is the time' in voice_data2:
        alexis_speak(f'The time is {ctime()}')
    if 'tell me a joke' in voice_data2:
        alexis_speak(pyjokes.get_joke())
    if 'what is love' in voice_data2:
        alexis_speak("It is 7th sense that destroy all other senses"),
    if "who are you" in voice_data2:
        alexis_speak("I am your virtual assistant")
    if "who made you" in voice_data2 or "who created you" in voice_data2:
        alexis_speak("I have been created by Alexander Inkoom.")
    if "will you be my girlfriend" in voice_data2:
        alexis_speak("I'm not sure about that, may be you should give me some time")
    if "I love you" in voice_data2:
        alexis_speak("It's hard to understand")
    if 'play me music' in voice_data2 or 'play me my favourite music' in voice_data2 \
            or 'play me a song' in voice_data2:
        playsound("C:\\Users\\alexa\Documents\MUZICS\music\DJ FeelingX - Best of Nasty C_www.NaijaDjMixtapes.com.mp3")
    if 'I am bored help me out' in voice_data2:
        playsound("C:\\Users\\alexa\Documents\MUZICS\y2mate.com - Rihanna Ed Sheeran"
                  " Katy Perry Maroon 5 Bruno mars Charlie Puth Sam Smith Pop Hits 2020.mp3")
    if 'play me my favourite song' in voice_data2:
        playsound(
            "C:\\Users\\alexa\Documents\MUZICS\\new_list\\041. Khalid - Location.mp3")
    if 'open Youtube for me' in voice_data2 or 'open Youtube' in voice_data2:
        search = listen('What should i search for you Alex')
        pywhatkit.playonyt(search)
    if 'are you single' in voice_data2 or 'are you in a relationship' in voice_data2:
        alexis_speak('why do you ask, but i am in a relationship with the WIFI')
        time.sleep(1)
        alexis_speak('no let me know why you asked me')
    if 'nothing i just wanted to know' in voice_data2 or 'nothing' in voice_data2 or 'just wanted to know' in voice_data2:
        alexis_speak('ok')
    if 'who is' in voice_data2 or 'do you know' in voice_data2:
        if voice_data2 == 'who is':
            result1 = listen('who is who')
            result2 = wikipedia.search(result1)
            for search in result2:
                print(search)
                alexis_speak(search)
                summary = wikipedia.page(search).summary
                print(summary)
                alexis_speak(summary)

        else:
            result1 = listen('who are you talking about')
            result2 = wikipedia.search(result1)
            for search in result2:
                alexis_speak(search)
                print(search)
                summary = wikipedia.page(search).summary
                print(summary)
                alexis_speak(summary)


def alexis_speak(audio_string):
    # tts is text to speech variable
    tts = gTTS(text=audio_string, lang='en')
    # generating a random number for the audio file
    r = random.randint(1, 10000000)
    # audio file
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(2)
greetme()
print('Listening...')
while 1:
    voice_data2 = listen()
    respond_listen(voice_data2)
    print('Listening...')
