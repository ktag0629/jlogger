#! /usr/bin/python3
from jlogger import JLog, Timestamp_level, Log_type
import argparse

def main():
    
    # parse arguments 
    parser = argparse.ArgumentParser(description="Write some logs!")
    parser.add_argument("--now", dest="timestamp_level", help="Timestamp to now")
    args = parser.parse_args()
    print(args)


main()
