# This is a simple help assistant/ help bot that allows to do basic things with it.

# All the necessary imports
from itertools import chain, cycle
import platform
import random
import time
import sys
import datetime
import webbrowser
import os

try:
    import wikipedia
except ModuleNotFoundError:
    print('The Library wikipedia was not found. Try pip install wikipedia')
    time.sleep(5)
    webbrowser.open('https://pypi.org/project/wikipedia/')
    time.sleep(2)
    sys.exit()

try:
    # noinspection PyUnresolvedReferences
    import pyttsx3
    # noinspection PyUnresolvedReferences
    import pyttsx3.drivers
    # noinspection PyUnresolvedReferences
    import pyttsx3.drivers.sapi5
except ModuleNotFoundError:
    print('The Library pyttsx3 was not found. Try pip install pyttsx3')
    time.sleep(5)
    webbrowser.open('https://pypi.org/project/pyttsx3/')
    time.sleep(2)
    sys.exit()

try:
    import speech_recognition
except ModuleNotFoundError:
    print('The Library speech_recognition was not found. Try pip install speechRecognition')
    time.sleep(5)
    webbrowser.open('https://pypi.org/project/SpeechRecognition/')
    time.sleep(2)
    sys.exit()
try:
    import module
except ModuleNotFoundError:
    print('The file module.py was not found! Are You Sure it is in the same directory?')
    time.sleep(5)
    webbrowser.open('https://github.com/MrAyushBajpai/SuperAI/blob/master/module.py')
    time.sleep(2)
    sys.exit()

try:
    import SpecialitesFinder
except ModuleNotFoundError:
    print('The file SpecialitesFinder was not found! Are You Sure it is in the same directory?')
    time.sleep(5)
    webbrowser.open('https://github.com/MrAyushBajpai/SuperAI/blob/master/SpecialitesFinder.py')
    time.sleep(2)
    sys.exit()

# Setting up configparser
import configparser

config = configparser.ConfigParser()
configfilepath = r'config.cfg'
config.read(configfilepath)

# All Necessary Variables
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[int(config.get('data-value', 'voice'))].id)
osinfo = str(platform.system()) + ' ' + str(platform.release()) + ' ' + str(platform.version())

# One time Code
module.logcat('START!!')
module.logcat('System is ' + str(osinfo))


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
        r.pause_threshold = int(config.get('data-value', 'pause_threshold'))
        r.energy_threshold = int(config.get('data-value', 'energy_threshold'))
        audio = r.listen(source)

    try:
        print('Processing....')
        print(' ')
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
        print()
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
        module.logcat('Checking ' + str(temp) + ' for Palindrome', False)
        if SpecialitesFinder.palindromechecker(temp):
            print('It is a palindrome string')
            speak('It is a palindrome string')
            module.logcat(str(temp) + ' is a palindrome string', False)
        else:
            print('It is not a palindrome string')
            speak('It is not a palindrome string')
            module.logcat(str(temp) + ' is not a palindrome string', False)

    elif 'armstrong' in cmd.lower() and 'check' in cmd.lower():
        speak('Enter the number to check for Armstrong: ')
        temp = recognize()
        module.logcat('Checking ' + str(temp) + ' for amrstrong number', False)
        try:
            temp = int(temp)
            if SpecialitesFinder.armstrongchecker(temp):
                print('It is an Armstrong Number')
                speak('It is an Armstrong Number')
                module.logcat(str(temp) + ' is an armstrong number', False)
            else:
                print('It is not an Armstrong Number')
                speak('It is not an Armstrong Number')
                module.logcat(str(temp) + ' is not an armstrong number', False)
        except ValueError:
            print('Only an Integer can be an armstrong number, so this is not an Armstrong number')
            speak('Only an Integer can be an armstrong number, so this is not an Armstrong number')
            module.logcat('ValueError while checking for Armstrong Number: Given Value - ' + str(temp), True)

    elif 'prime' in cmd.lower() and 'check' in cmd.lower():
        speak('Enter the number to check for Prime Number')
        temp = recognize()
        module.logcat('Checking ' + str(temp) + ' for prime or not')
        try:
            temp = int(temp)
            if SpecialitesFinder.primechecker(temp):
                print('It is a Prime Number.')
                speak('It is a Prime Number.')
                module.logcat(str(temp) + ' is a prime number')
            else:
                print('It is not a Prime Number')
                speak('It is not a Prime Number')
                module.logcat(str(temp) + ' is not a prime number')
        except ValueError:
            print('Only an integer can be a Prime Number, so this is not a Prime Number')
            speak('Only an integer can be a Prime Number, so this is not a Prime Number')
            module.logcat('ValueError while checking for prime: Given Value - ' + str(temp), True)

    elif 'wikipedia' in cmd.lower():
        speak('Searching Wikipedia!....')
        query = cmd.lower().replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak('According to Wikipedia')
        speak(results)
        module.logcat('Search Wikipedia for ' + query, False)

    elif 'open' in cmd.lower() and 'google' in cmd.lower():
        speak('Opening Google')
        url = 'https://www.google.com'
        module.logcat('Opening "' + url + '" in webbrowser')
        webbrowser.open(url)

    elif 'open' in cmd.lower() and 'youtube' in cmd.lower():
        speak('Opening YouTube')
        url = 'https://www.youtube.com'
        module.logcat('Opening "' + url + '" in webbrowser')
        webbrowser.open(url)

    elif 'open' in cmd.lower() and ('stack' in cmd.lower() or 'overflow' in cmd.lower()):
        speak('Opening Stack Overflow')
        url = 'https://stackoverflow.com/'
        module.logcat('Opening "' + url + '" in webbrowser')
        webbrowser.open(url)

    elif 'open' in cmd.lower() and ('git' in cmd.lower() and 'hub' in cmd.lower()):
        speak('Opening GitHub')
        url = 'https://github.com'
        module.logcat('Opening "' + url + '" in webbrowser')
        webbrowser.open(url)

    elif 'search' in cmd.lower():
        cmd = cmd.lower()
        query = list(chain(*zip(cmd.split(), cycle(' '))))[:-1]
        tester = 'google'
        min_dist = len(query) + 1
        for i in ['google', 'bing', 'yahoo', 'duckduckgo', 'duck']:
            if i in query:
                tester = i
                for index in range(len(query)):
                    if query[index] == 'search':
                        for search in range(len(query)):
                            if query[search] == i:
                                curr = abs(index - search) - 1
                                if curr < min_dist:
                                    min_dist = curr
        if min_dist <= 4 and min_dist < (len(query) + 1):
            del query[query.index('search'):query.index(tester) + 1]
        if query[0] == ' ':
            del query[0]
        speak('Searching')
        if tester == 'google':
            del query[query.index('search')]
            query = ''.join(query)
            url = 'https://www.google.com/search?q=' + query
            module.logcat('Opening "' + url + '" in webbrowser')
            webbrowser.open(url)
        elif tester == 'bing':
            query = ''.join(query)
            url = 'https://www.bing.com/search?q=' + query
            module.logcat('Opening "' + url + '" in webbrowser')
            webbrowser.open(url)
        elif tester == 'duckduckgo' or tester == 'duck':
            query = ''.join(query)
            url = 'https://duckduckgo.com/?q=' + query
            module.logcat('Opening "' + url + '" in webbrowser')
            webbrowser.open(url)
        elif tester == 'yahoo':
            query = ''.join(query)
            url = 'https://search.yahoo.com/search?p=' + query
            module.logcat('Opening "' + url + '" in webbrowser')
            webbrowser.open(url)

    elif 'time' in cmd.lower():
        strtime = datetime.datetime.now().strftime('%H %M')
        print(datetime.datetime.now().strftime('%H:%M'))
        speak('Time is' + strtime)
        module.logcat('Retrived Current time as ' + strtime, False)

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
            module.logcat('Loaded from wikipedia about ' + query, False)
        except Exception:
            url = 'https://www.google.com/search?q=' + cmd
            module.logcat('Opening "' + url + '" in webbrowser', False)
            webbrowser.open(url)

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
            module.logcat('Loaded from wikipedia about ' + query, False)
        except Exception:
            url = 'https://www.google.com/search?q=' + cmd
            module.logcat('Opening "' + url + '" in webbrowser', False)
            webbrowser.open(url)

    elif 'how' in cmd.lower() or 'when' in cmd.lower():
        url = 'https://www.google.com/search?q=' + cmd
        module.logcat('Opening "' + url + '" in webbrowser', False)
        webbrowser.open(url)

    elif 'morning' in cmd.lower():
        print('Good Morning!')
        speak('Good Morning')

    elif 'afternoon' in cmd.lower():
        print('Good Afternoon!')
        speak('Good Afternoon')
    elif 'evening' in cmd.lower():
        print('Good Evening!')
        speak('Good Evening')

    elif 'night' in cmd.lower():
        print('Good Night!')
        speak('Good Night')

    elif 'even' in cmd.lower() or 'odd' in cmd.lower():
        speak('Enter the number to check for even or odd')
        print('Enter the number to check for even or odd')
        temp = recognize()
        module.logcat('Checking ' + str(temp) + ' for even or odd.', False)
        try:
            temp = int(temp)
            if SpecialitesFinder.evenorodd(temp):
                print('It is an even number.')
                speak('It is an even number.')
                module.logcat(str(temp) + ' is an even number', False)
            else:
                print('It is an odd number')
                speak('It is an odd number')
                module.logcat(str(temp) + ' is an odd number', False)
        except ValueError:
            print('Whatever you entered seems not be an integer, so yeah.')
            speak('Whatever you entered seems not be an integer, so yeah.')

    elif 'quit' in cmd.lower() or 'exit' in cmd.lower() or ('close' in cmd.lower() and 'program' in cmd.lower()):
        print('Closing the Program. Hope to see you soon!')
        speak('Closing the Program. Hope to see you soon!')
        module.logcat('Program Exit!', False)
        sys.exit()
