# This is a simple help assistant/ help bot that allows to do basic things with it.

# All the necessary imports
from itertools import chain, cycle
import platform
import random
import time
import sys
import pyttsx3
import speech_recognition
import wikipedia
import datetime
import webbrowser

try:
    import module
except ModuleNotFoundError:
    print('The file module.py was not found! Are You Sure it is in the same directory?')
    time.sleep(5)
    sys.exit()

try:
    import SpecialitesFinder
except ModuleNotFoundError:
    print('The file SpecialitesFinder was not found! Are You Sure it is in the same directory?')
    time.sleep(5)
    sys.exit()

import os

# Setting up configparser
import configparser
config = configparser.ConfigParser()
configfilepath = r'config.cfg'
config.read(configfilepath)

# All Necessary Variables
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# All the necessary functions
def randomgenerator(rmin, rmax):
    return random.randint(rmin, rmax)


def speak(statement):
    engine.say(statement)
    engine.runAndWait()


def recognize():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Processing....')
        command = r.recognize_google(audio, language='en-in')
        print('User Command - ', command)
    except Exception:
        print('Can you repeat please')
        return 'None'
    return command


# One time code
if not os.path.exists(config.get('file-path', 'logfilepath')):
    os.mkdir(config.get('file-path', 'logfilepath'))
print(module.timeset(), 'Welcome to SuperAI!')
speak(module.timeset())
speak('Welcome to SuperAI')

# Main Loop that runs forever
while True:
    # Loop so that if the cmd entered is empty, program can be faster by just looping here again
    while True:
        cmd = recognize()
        print(' ')
        if cmd != '':
            module.logcat('Command Entered is -- ' + cmd)
            break
        else:
            continue

    # Checks for the entered command
    if 'how are you' in cmd.lower() or 'how you doing' in cmd.lower():
        num = randomgenerator(1, 6)
        if num == 1:
            print('I am doing Great! How are You?')
            speak('I am doing Great! How are You?')
        elif num == 2:
            print('I am constantly updated. That\'s how I am doing.')
            speak('I am constantly updated. That is how I am doing.')
        elif num == 3:
            print('My Existence is non emotional. The only thing I do good is probably helping you.')
            speak('My Existence is non emotional. The only thing I do good is probably helping you.')
        elif num == 4:
            print('I may not be the best, but I certainly enjoy being myself!')
            speak('I may not be the best, but I certainly enjoy being myself!')
        elif num == 5:
            print('Good.')
            speak('Good')
        elif num == 6:
            print('With you on my side, I am unstoppable!')
            speak('With you on my side, I am unstoppable!')

    elif 'operating system' in cmd.lower():
        print(platform.system(), platform.release(), platform.version())
        speak(platform.system() + platform.release() + platform.version())

    elif 'hello' in cmd.lower() or 'hi' in cmd.lower() or 'howdy' in cmd.lower() or cmd.lower() == 'hey':
        num = randomgenerator(1, 6)
        if num == 1:
            print('Hello! How are You?')
            speak('Hello! How are You?')
        elif num == 2:
            print('Hieeee!')
            speak('Hieeee!')
        elif num == 3:
            print('Hey! How you doing?')
            speak('Hey! How you doing?')
        elif num == 4:
            print('Howdy Mate!')
            speak('Howdy Mate!')
        elif num == 5:
            print('Greetings!')
            speak('Greetings!')
        elif num == 6:
            print('Bonjour! Nice to Meet You.')
            speak('Bonjour! Nice to Meet You.')

    elif 'palindrom' in cmd.lower() and 'check' in cmd.lower():
        speak('Enter the string to check for Palindrome')
        temp = recognize()
        if SpecialitesFinder.palindromechecker(temp):
            print('It is a palindrome string')
            speak('It is a palindrome string')
        else:
            print('It is not a palindrome string')
            speak('It is not a palindrome string')

    elif 'armstrong' in cmd.lower() and 'check' in cmd.lower():
        speak('Enter the number to check for Armstrong: ')
        temp = recognize()
        try:
            temp = int(temp)
            if SpecialitesFinder.armstrongchecker(temp):
                print('It is an Armstrong Number')
                speak('It is an Armstrong Number')
            else:
                print('It is not an Armstrong Number')
                speak('It is not an Armstrong Number')
        except ValueError:
            print('Only an Integer can be an armstrong number, so this is not an Armstrong number')
            speak('Only an Integer can be an armstrong number, so this is not an Armstrong number')

    elif 'prime' in cmd.lower() and 'check' in cmd.lower():
        speak('Enter the number to check for Prime Number')
        temp = recognize()
        try:
            temp = int(temp)
            if SpecialitesFinder.primechecker(temp):
                print('It is a Prime Number.')
                speak('It is a Prime Number.')
            else:
                print('It is not a Prime Number')
                speak('It is not a Prime Number')
        except ValueError:
            print('Only an integer can be a Prime Number, so this is not a Prime Number')
            speak('Only an integer can be a Prime Number, so this is not a Prime Number')

    elif 'wikipedia' in cmd.lower():
        speak('Searching Wikipedia!....')
        query = cmd.lower().replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak('According to Wikipedia')
        speak(results)

    elif 'open' in cmd.lower() and 'google' in cmd.lower():
        speak('Opening Google')
        webbrowser.open('https://www.google.com')

    elif 'open' in cmd.lower() and 'youtube' in cmd.lower():
        speak('Opening YouTube')
        webbrowser.open('https://www.youtube.com')

    elif 'open' in cmd.lower() and ('stack' in cmd.lower() or 'overflow' in cmd.lower()):
        speak('Opening Stack Overflow')
        webbrowser.open('https://stackoverflow.com/')

    elif 'open' in cmd.lower() and ('git' in cmd.lower() and 'hub' in cmd.lower()):
        speak('Opening GitHub')
        webbrowser.open('https://github.com')

    elif 'search' in cmd.lower():
        cmd = cmd.lower().replace('search', '')
        cmd.replace(' ', '+')
        speak('Searching')
        webbrowser.open('https://www.google.com/search?q=' + cmd)

    elif 'time' in cmd.lower():
        strtime = datetime.datetime.now().strftime('%H %M')
        print(datetime.datetime.now().strftime('%H:%M'))
        speak('Time is' + strtime)

    elif 'what' in cmd.lower():
        query = list(chain(*zip(cmd.split(), cycle(' '))))[:-1]
        if 'what' in query:
            tmp1 = query.index('what')
            if 'is' in query:
                tmp2 = query.index('is')
                if tmp1 + 1 == tmp2:
                    del query[tmp1:tmp2 + 1]
            elif 'are' in query:
                tmp2 = query.index('are')
                if tmp1 + 1 == tmp2:
                    del query[tmp1:tmp2 + 1]
            else:
                del query[tmp1]
        query = ''.join(query)
        try:
            speak('Just a second')
            results = wikipedia.summary(cmd, sentences=2)
            print(results)
            speak('According to Wikipedia')
            speak(results)
        except Exception:
            webbrowser.open('https://www.google.com/search?q=' + cmd)

    elif 'who' in cmd.lower():
        print(cmd)
        query = list(chain(*zip(cmd.split(), cycle(' '))))[:-1]
        if 'who' in query:
            tmp1 = query.index('who')
            if 'is' in query:
                tmp2 = query.index('is')
                if tmp1 + 2 == tmp2 or tmp1 + 1 == tmp2:
                    del query[tmp1:tmp2 + 1]
            elif 'are' in query:
                tmp2 = query.index('are')
                if tmp1 + 1 == tmp2:
                    del query[tmp1:tmp2 + 1]
            else:
                del query[tmp1]
        query = ''.join(query)
        try:
            speak('Just a second')
            results = wikipedia.summary(cmd, sentences=2)
            print(results)
            speak('According to Wikipedia')
            speak(results)
        except Exception:
            webbrowser.open('https://www.google.com/search?q=' + cmd)

    elif 'how' in cmd.lower():
        webbrowser.open('https://www.google.com/search?q=' + cmd)

    elif 'even' in cmd.lower() or 'odd' in cmd.lower():
        speak('Enter the number to check for even or odd')
        print('Enter the number to check for even or odd')
        temp = recognize()
        try:
            temp = int(temp)
            if SpecialitesFinder.evenorodd(temp):
                print('It is an even number.')
                speak('It is an even number.')
            else:
                print('It is an odd number')
                speak('It is an odd number')
        except ValueError:
            print('Whatever you entered seems not be an integer, so yeah.')
            speak('Whatever you entered seems not be an integer, so yeah.')

    elif 'quit' in cmd.lower() or 'exit' in cmd.lower() or ('close' in cmd.lower() and 'program' in cmd.lower()):
        print('Closing the Program. Hope to see you soon!')
        speak('Closing the Program. Hope to see you soon!')
        sys.exit()
