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
    import special
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

    # noinspection PyBroadException
    try:
        print('Processing....')
        print(' ')
        command = r.recognize_google(audio, language='en-in')
        print('User Command - ', command)
    except Exception:
        print('Can you repeat please')
        print(' ')
        return 'None'
    return command


# One time code
if not os.path.exists(config.get('file-path', 'logfilepath')):
    os.makedirs(config.get('file-path', 'logfilepath'))
print(module.timeset(), f'Welcome {config.get("user-info", "name")}')
module.logcat('START!!')
module.logcat(f'System is {str(osinfo)}')
speak(module.timeset())
speak(f'Welcome {config.get("user-info", "name")}')

# Main Loop that runs forever
while True:
    # Loop so that if the cmd entered is empty, program can be faster by just looping here again
    while True:
        cmd = recognize()
        print(' ')
        if cmd != 'None':
            break
        else:
            continue
    # Used to check if the command entered is specific to SuperAI
    if 'super' not in cmd.lower():
        continue
    else:
        query = list(chain(*zip(cmd.split(), cycle(' '))))[:-1]
        # noinspection PyBroadException
        try:
            del query[query.index('super')]
        except Exception:
            del query[query.index('Super')]
        cmd = ''.join(query)
        module.logcat('Command Entered is -- ' + cmd)

    # Checks for the entered command
    if 'search' in cmd.lower():
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

    elif 'operating system' in cmd.lower():
        print()
        speak(platform.system() + platform.release() + platform.version())

    elif 'palindrom' in cmd.lower() and 'check' in cmd.lower():
        speak('Enter the string to check for Palindrome')
        temp = recognize()
        if temp != 'None':
            module.logcat('Checking ' + str(temp) + ' for Palindrome', False)
            if special.palindromechecker(temp):
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
        if temp != 'None':
            module.logcat('Checking ' + str(temp) + ' for amrstrong number', False)
            try:
                temp = int(temp)
                if special.armstrongchecker(temp):
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
        if temp != 'None':
            module.logcat('Checking ' + str(temp) + ' for prime or not')
            try:
                temp = int(temp)
                if special.primechecker(temp):
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

    elif 'even' in cmd.lower() or 'odd' in cmd.lower():
        speak('Enter the number to check for even or odd')
        print('Enter the number to check for even or odd')
        temp = recognize()
        if temp != 'None':
            module.logcat('Checking ' + str(temp) + ' for even or odd.', False)
            try:
                temp = int(temp)
                if special.evenorodd(temp):
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

    elif 'open' in cmd.lower():
        if 'google' in cmd.lower():
            speak('Opening Google')
            url = 'https://www.google.com'
            module.logcat(f'Opening {url} in webbrowser')
            webbrowser.open(url)

        elif 'youtube' in cmd.lower():
            speak('Opening YouTube')
            url = 'https://www.youtube.com'
            module.logcat(f'Opening {url} in webbrowser')
            webbrowser.open(url)

        elif 'stack' in cmd.lower() or 'overflow' in cmd.lower():
            speak('Opening Stack Overflow')
            url = 'https://stackoverflow.com/'
            module.logcat(f'Opening {url} in webbrowser')
            webbrowser.open(url)

        elif 'git' in cmd.lower() and 'hub' in cmd.lower():
            speak('Opening GitHub')
            url = 'https://github.com'
            module.logcat(f'Opening {url} in webbrowser')
            webbrowser.open(url)

        elif 'wik' in cmd.lower() or 'vic' in cmd.lower():
            if 'how' in cmd.lower():
                speak('Opening Wikihow')
                url = 'https://www.wikihow.com/'
            elif 'common' in cmd.lower():
                speak('Opeing Wikimedia Commons')
                url = 'https://commons.wikimedia.org/'
            elif 'meta' in cmd.lower():
                speak('Opening Meta Wiki')
                url = 'https://meta.wikimedia.org/'
            elif 'incubator' in cmd.lower():
                speak('Opening Wikimedia Incubator')
                url = 'https://incubator.wikimedia.org/'
            elif 'tech' in cmd.lower() or 'cloud' in cmd.lower():
                speak('Opening Wikitech')
                url = 'https://wikitech.wikimedia.org/'
            elif 'foundation' in cmd.lower():
                speak('Opening Wikimedia Foundation')
                url = 'https://wikimediafoundation.org/'
            elif 'wikimedia' in cmd.lower():
                speak('Opening Wikimedia')
                url = 'https://www.wikimedia.org/'
            elif 'mediawiki' in cmd.lower():
                speak('Opening Mediawiki')
                url = 'https://www.mediawiki.org/'
            elif 'tionary' in cmd.lower():
                speak('Opening Wiktionary')
                url = 'https://www.wiktionary.org/'
            elif 'quote' in cmd.lower():
                speak('Opening Wikiquote')
                url = 'https://www.wikiquote.org/'
            elif 'book' in cmd.lower():
                speak('Opening Wikibooks')
                url = 'https://www.wikibooks.org/'
            elif 'source' in cmd.lower():
                speak('Opening Wikisource')
                url = 'https://wikisource.org/'
            elif 'news' in cmd.lower():
                speak('Opening Wikinews')
                url = 'https://www.wikinews.org/'
            elif 'versity' in cmd.lower():
                speak('Opening Wikiversity')
                url = 'https://www.wikiversity.org/'
            elif 'species' in cmd.lower():
                speak('Opening Wikispecies')
                url = 'https://species.wikimedia.org/'
            elif 'data' in cmd.lower():
                speak('Opening Wikidata')
                url = 'https://www.wikidata.org/'
            elif 'voyage' in cmd.lower():
                speak('Opening Wikivoyage')
                url = 'https://www.wikivoyage.org/'
            else:
                speak('Opening Wikipedia')
                url = 'https://www.wikipedia.org/'

            module.logcat(f'Opening {url} in webbrowser')
            webbrowser.open(url)

    elif 'wikipedia' in cmd.lower():
        speak('Searching Wikipedia!....')
        query = cmd.lower().replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak('According to Wikipedia')
        speak(results)
        module.logcat('Search Wikipedia for ' + query, False)

    elif 'time' in cmd.lower():
        strtime = datetime.datetime.now().strftime('%H %M')
        print(datetime.datetime.now().strftime('%H:%M'))
        speak('Time is' + strtime)
        module.logcat('Retrived Current time as ' + strtime, False)

    elif 'what' in cmd.lower():
        if 'what is your name' in cmd.lower():
            print('My Name is SuperAI.')
            speak('My Name is SuperAI')

        elif 'what is my name' in cmd.lower():
            name = config.get("user-info", "name")
            if name != 'to SuperAI':
                print(f'You are {name}')
                speak(f'You are {name}')
            else:
                print("I don't know what your name is.")
                speak("I don't know what your name is.")
        elif 'age' in cmd.lower():
            age = module.agecalc(int(config.get("user-info", "day")), int(config.get("user-info", "month")),
                                 int(config.get("user-info", "year")))
            if age <= 0:
                print("I don't know your date of birth")
                speak("I don't know your date of birth")
            else:
                print(f'Your age is {age}')
                speak(f'Your age is {age}')

        elif 'birth' in cmd.lower() or 'born' in cmd.lower():
            # noinspection PyBroadException
            try:
                if config.get("user-info", "day") == '0':
                    print("I don't know your date of birth")
                    speak("I don't know your date of birth")
                else:
                    tmpdate = module.birthdate(int(config.get("user-info", "day")),
                                               int(config.get("user-info", "month")),
                                               int(config.get("user-info", "year")))
                    print(f'Your Birthdate is {tmpdate}')
                    speak(f'Your Birthdate is {tmpdate}')
            except Exception:
                print("I don't know about your date of birth.")

        else:
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
            # noinspection PyBroadException
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

    elif 'when' in cmd.lower():
        if 'birth' in cmd.lower() or 'born' in cmd.lower():
            if 'you' not in cmd.lower():
                # noinspection PyBroadException
                try:
                    if config.get("user-info", "day") == '0':
                        print("I don't know your date of birth")
                        speak("I don't know your date of birth")
                    else:
                        tmpdate = module.birthdate(int(config.get("user-info", "day")),
                                                   int(config.get("user-info", "month")),
                                                   int(config.get("user-info", "year")))
                        print(f'Your Birthdate is {tmpdate}')
                        speak(f'Your Birthdate is {tmpdate}')
                except Exception:
                    print("I don't know about your date of birth.")
        else:
            url = f'https://www.google.com/search?q={cmd}'
            module.logcat(f'Opening {url} in webbrowser', False)
            webbrowser.open(url)

    elif 'how' in cmd.lower():
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
        else:
            url = f'https://www.google.com/search?q={cmd}'
            module.logcat(f'Opening {url} in webbrowser', False)
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
        # noinspection PyBroadException
        try:
            speak('Just a second')
            results = wikipedia.summary(cmd, sentences=2)
            print(results)
            speak('According to Wikipedia')
            speak(results)
            module.logcat('Loaded from wikipedia about ' + query, False)
        except Exception:
            url = f'https://www.google.com/search?q={cmd}'
            module.logcat('Opening "' + url + '" in webbrowser', False)
            webbrowser.open(url)

    elif 'privacy' in cmd.lower():
        if 'on' in cmd.lower() or 'start' in cmd.lower():
            print('Turning on Privacy Mode!')
            speak('Turning on Privacy Mode!')
            config.set("toggles", "keeplog", "False")
            with open(r'config.cfg', 'w') as f:
                config.write(f)
                f.close()
        elif 'off' in cmd.lower() or 'stop' in cmd.lower():
            print('Turning off Privacy Mode!')
            speak('Turning off Privacy Mode!')
            config.set("toggles", "keeplog", "True")
            with open(r'config.cfg', 'w') as f:
                config.write(f)
                f.close()

    elif 'name' in cmd.lower():
        while True:
            print('Please tell me your name')
            speak('Please tell me your name')
            name = recognize()
            if name == 'None':
                print('Please tell the name again')
                speak('Please tell the name again')
                continue
            while True:
                print(f'The Name is - {name.title()}. Is that correct? Or you want to change?')
                speak(f'The Name is - {name.title()}. Is that correct? Or you want to change?')
                tester = recognize()
                if tester == 'None':
                    continue
                else:
                    break
            if 'y' in tester.lower():
                module.logcat(f'Name changed to -- {name.title()} from --  {config.get("user-info", "name")}', False)
                config.set("user-info", "name", name.title())
                with open(r'config.cfg', 'w') as f:
                    config.write(f)
                    f.close()
                print(f'Name is now set to {name.title()}')
                speak(f'Name is now set to {name.title()}')
                break
            else:
                continue

    elif 'birth' in cmd.lower() and ('date' in cmd.lower() or 'day' in cmd.lower()):
        while True:
            print('What is the date you were born(just the day of the month)?')
            speak('What is the date you were born(just the day of the month)?')
            day = recognize()
            try:
                day = int(day)
            except ValueError:
                print("Sorry, Let's Try Again")
                speak("Sorry, Let's Try Again")
                continue
            if 1 <= day <= 31:
                break

        while True:
            print('What is the month you were born, in numerical?')
            speak('What is the month you were born, in numerical?')
            month = recognize()
            try:
                month = int(month)
            except ValueError:
                print("Sorry, Let's Try Again")
                speak("Sorry, Let's Try Again")
                continue
            if 1 <= month <= 12:
                break

        while True:
            print('What is the year in which you were born?')
            speak('What is the year in which you were born?')
            year = recognize()
            try:
                year = int(year)
            except ValueError:
                print("Sorry, Let's Try Again")
                speak("Sorry, Let's Try Again")
                continue
            break
        tmpdate = module.birthdate(day, month, year)
        if not tmpdate:
            print('Invalid Date. This month does not have these many days!')
            speak('Invalid Date. This month does not have these many days!')
        elif tmpdate == 'traveller':
            print("Are You a Time Traveller? How are you born in the future?")
            speak("Are You a Time Traveller? How are you born in the future?")
        else:
            print(f'Is this correct? {tmpdate}')
            speak(f'Is this correct?, {tmpdate}')
            tester = recognize()
            if 'y' in tester.lower():
                config.set("user-info", "day", str(day))
                config.set("user-info", "month", str(month))
                config.set("user-info", "year", str(year))
                with open(r'config.cfg', 'w') as f:
                    config.write(f)
                    f.close()
                print(f'Your birthdate has been changed to {tmpdate}')
                speak(f'Your birthdate has been changed to {tmpdate}')
            else:
                print('Your birthdate was not changed!')
                speak('Your birthdate was not changed!')

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

    elif 'quit' in cmd.lower() or 'exit' in cmd.lower() or ('close' in cmd.lower() and 'program' in cmd.lower()):
        print('Closing the Program. Hope to see you soon!')
        speak('Closing the Program. Hope to see you soon!')
        module.logcat('Program Exit!', False)
        sys.exit()

    else:
        print("I don't get what you mean..... You want me to search that on the web?")
        speak("I don't get what you mean..... You want me to search that on the web?")
        tester = recognize()
        if 'y' in tester.lower():
            url = f'https://www.google.com/search?q={cmd}'
            module.logcat('Opening "' + url + '" in webbrowser', False)
            webbrowser.open(url)
