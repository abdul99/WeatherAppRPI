__author__ = 'mike'
# Display the current time to the lcd for the given number of seconds
import time
from time import strftime


class DisplayTime:
    lcd = None

    def __init__(self, lcd):
        self.lcd = lcd

    def run(self, seconds):
        self.lcd.clear()
        while seconds > 0:
            self.lcd.home()
            self.lcd.message(strftime("%H:%M:%S") + '\n' + strftime("%Y-%m-%d"))
            time.sleep(1.0)
            seconds = (seconds - 1)

