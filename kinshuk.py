pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install pywhatkit
pip install wikipedia

import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as data_taker:
    print("Say Something")
    voice = listener.listen(data_taker)
    instruct = listener.recognize_google(voice)
    instruct = instruct.lower()
    print(instruct)
except:
    pass

import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as data_taker:
    print("Say Something")
    voice = listener.listen(data_taker)
    instruct = listener.recognize_google(voice)
    instruct = instruct.lower()
    print(instruct)
    if'Max' in instruct:
        print(instruct)
except:
    pass

import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('hey Sir how are you')
engine.say('Hey what you want')
engine.runAndWait()

try:
    with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        print(instruct)
        if'Max' in instruct:
            print(instruct)
except:
    pass

import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        print(instruct)
        if'Max' in instruct:
            print(instruct)
    except:
        pass
def run_Max():
    instruct = take_command()
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing' + song)
        print(song)

run_Max()

import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        print(instruct)
        if'Max' in instruct:

            instruct = instruct.replace('Max', '')
            print(instruct)
    except:
        pass
def run_Max():
    instruct = take_command()
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        print(song)

run_Max()

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        print(instruct)
        if'Max' in instruct:

            instruct = instruct.replace('Max', '')
            print(instruct)
    except:
        pass
def run_Max():
    instruct = take_command()
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in instruct:
        time = datetime.datetime.now().strftime('%I: %M')
        print(time)
        talk('current time is' + time)
    elif 'tell me about' in instruct:
        thing = instruct.replace('tell me about', '')
        info = wikipedia.summary(thing, 2)
        print(info)
        talk(info)

run_Max()

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as data_taker:
        print("Say Somethig")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        if'Max' in instruct:
            instruct = instruct.replace('Max', '')
            print(instruct)
    except:
        pass
    return instruct

def run_Max():
    instruct = take_command()
    if 'play' in instruct:
        song = instruct.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruct:
        time = datetime.datetime.now().strftime('%I: %M')
        print(time)
        talk('current time is' + time)
    elif 'tell me about' in instruct:
        thing = instruct.replace('tell me about', '')
        info = wikipedia.summary(thing, 2)
        print(info)
        talk(info)
     elif 'who are you' in instruct:
         talk('I am your personal Assistant Max')
     elif 'what can you do for me' in instruct:
         talk('I can play songs, tell time, and help you go with wikipedia')
     else:
         talk('I did not understand, can you repeat again')

while True: 
    run_Max()


