#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time
from time import strftime

class DisplayTime:
    lcd = None

    def __init__(self, lcd):
        DisplayTime.lcd = lcd

    @staticmethod
    def run(seconds):
        DisplayTime.lcd.clear()
        while seconds > 0:
            DisplayTime.lcd.home()
            DisplayTime.lcd.message(strftime("%H:%M:%S") + '\n' + strftime("%Y-%m-%d"))
            time.sleep(0.8)  # Print a two line message
            seconds = (seconds - 1)


# Demo showing the cursor.
#lcd.show_cursor(True)
#lcd.blink(True)

# Demo scrolling message right/left.
#lcd.clear()
#message = 'Scroll'
#lcd.message(message)
#for i in range(lcd_columns-len(message)):
#	time.sleep(0.5)
#	lcd.move_right()
#for i in range(lcd_columns-len(message)):
#	time.sleep(0.5)
#	lcd.move_left()
