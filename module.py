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
