# Necessary Imports
import os
import time
import sys
from datetime import datetime

# Setting up configparser
import configparser

config = configparser.ConfigParser()
configfilepath = r'config.cfg'
config.read(configfilepath)

# Necessary Variables
try:
    logfile = os.path.join(config.get('file-path', 'logfilepath'), config.get('file-path', 'logfilename'))
except configparser.NoSectionError:
    print('There is an issue with the config.cfg file. It either doesn\'t exist, or is modified in a wrong way')
    time.sleep(5)
    sys.exit()


# Function for logging events and errors
def logcat(event, iserror=False):
    if config.get("toggles", "keeplog").lower() == 'true':
        now = datetime.now()
        current_datetime = now.strftime("[%D::%H:%M:%S]")
        if iserror:
            lf = open(logfile, 'a')
            lf.write('@!! ' + current_datetime + ' -- ' + event)
            lf.write('\n')
            lf.close()
        else:
            lf = open(logfile, 'a+')
            lf.write(current_datetime + ' -- ' + event)
            lf.write('\n')
            lf.close()


def timeset():
    current_hour = int(datetime.now().hour)
    if 0 <= current_hour < 12:
        return 'Good Morning!'
    elif 12 <= current_hour < 18:
        return 'Good Afternoon!'
    else:
        return 'Good Evening!'


def agecalc(day: int, month: int, year: int):
    if year == 0:
        return 0
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    if month < current_month or day < current_day:
        return int(current_year - year - 1)
    return int(current_year - year)


def birthdate(day: int, month: int, year: int):
    mddict = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    mndict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    if month == 2:
        if year % 4 == 0:
            mddict[2] = 29
        else:
            mddict[2] = 28
    if day > mddict[month]:
        return False
    if year > int(datetime.now().year):
        return 'traveller'
    return f'{day} {mndict[month]}, {year}'
