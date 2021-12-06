from enum import Enum
from datetime import datetime
import appdirs

class Timestamp_level(Enum):
    NOW = 1
    TODAY = 2
    DATE = 3

class Log_type(Enum):
    LOG = 1
    TASK = 2
    #EVENT = 3 # coming soon

class JLog:
    
    def __init__(tstamp_level, log_type):
        self._tstamp_level = tstamp_level
        self._log_type = log_type

