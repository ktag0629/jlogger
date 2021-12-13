from enum import Enum
from datetime import datetime
import os

class Timestamp_level(Enum):
    NOW = 1
    #TODAY = 2
    #DATE = 3

class Log_type(Enum):
    LOG = 1
    TASK = 2
    #EVENT = 3 # coming soon

class JLog:
    
    def __init__(self, tstamp_level, log_type):
        self._tstamp_level = tstamp_level
        self._log_type = log_type
        self._log_dir = os.path.join(os.path.expanduser("~"), "JLOGS")
        if not os.path.isdir(self._log_dir):
            os.mkdir(self._log_dir)

    def write_to_log(self, message):

        # sanitize messgae
        message = message.strip()

        timestamp_format = "[%Y-%m-%d %I:%M %p]"
        timestamp = datetime.now().strftime(timestamp_format) # uses local time

        logfile = os.path.join(self._log_dir, "main.log")
        with open(logfile, "a+") as lf:
            lf.write(timestamp + " " + message + "\n")

    def list_last_logs(self, count=10):

        logfile = os.path.join(self._log_dir, "main.log")
        with open(logfile, "r") as lf:
            for line in (lf.readlines()[-count:]):
                print(line, end='')
