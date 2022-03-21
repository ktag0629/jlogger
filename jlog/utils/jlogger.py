"""
Author: Kent Taguba
Contains:
    * Timestamp Enum
    * Log type Enum
    * JLog class
"""
from enum import Enum
from datetime import datetime
import os

class TimestampLevel(Enum):
    """enums for timestaml levels[TODO]"""
    NOW = 1
    #TODAY = 2
    #DATE = 3

class LogType(Enum):
    """log types[TODO]"""
    LOG = 1
    TASK = 2
    #EVENT = 3 # coming soon

class JLog:
    """functions that write and displays(list) logs"""
    def __init__(self, tstamp_level, log_type):
        self._tstamp_level = tstamp_level
        self._log_type = log_type
        self._log_dir = os.path.join(os.path.expanduser("~"), "JLOGS")
        now = datetime.now()
        self._log_file = os.path.join(self._log_dir,
                                      f"{now.year}.{now.month}.{now.day}.log")
        if not os.path.isdir(self._log_dir):
            os.mkdir(self._log_dir)

    def write_to_log(self, message):
        """writes the message to the log file

        Creates a timestamp for each message and writes the message on discrete
            lines within the log file

        Args:
        message -> str:
            the log message

        Returns:
        None

        Asserts:
        None
        """
        message = message.strip()

        timestamp_format = "[%Y-%m-%d %I:%M %p]"
        timestamp = datetime.now().strftime(timestamp_format) # uses local time

        with open(self._log_file, "a+") as log_file:
            log_file.write(timestamp + " " + message + "\n")

    def list_last_logs(self, lines=10):
        """Displays the last `count` lines of the log file

        Args:
        lines -> int:
            lines of log to list

        Returns:
        None

        Asserts:
        None
        """

        with open(self._log_file, "r") as log_file:
            for line in (log_file.readlines()[-lines:]):
                print(line, end='')
