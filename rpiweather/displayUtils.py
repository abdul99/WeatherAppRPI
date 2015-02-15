# custom lcd utilities for rpi connected LCD
__author__ = 'mike'
import time


class DisplayUtils:
    lcd = None
    scrollSpeed = 0.7
    pauseTime = 2.0


    def __init__(self, lcd):
        DisplayUtils.lcd = lcd

    def backAndForth(self, line1, line2, repeat):

        # display first 16 chars of each
        DisplayUtils.lcd.message(line1 + '\n')
        DisplayUtils.lcd.message(line2)

        # max scrolling length is longest line
        maxLength = 0
        if len(line1) > len(line2):
            maxLength = len(line1)
        else:
            maxLength = len(line2)

        # scroll both directions 'repeat' number of times
        for i in range(repeat):
            if maxLength > 16:
                time.sleep(DisplayUtils.pauseTime)  # small pause before moving
                # move lcd text all the way left
                for i in range(maxLength - 16):
                    time.sleep(DisplayUtils.scrollSpeed)
                    DisplayUtils.lcd.move_left()

                time.sleep(DisplayUtils.pauseTime)  # small pause before moving back
                # move lcd text back to original position
                for i in range(maxLength - 16):
                    time.sleep(DisplayUtils.scrollSpeed)
                    DisplayUtils.lcd.move_right()