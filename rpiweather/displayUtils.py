# custom lcd utilities for rpi connected LCD
__author__ = 'mike'
import time


class DisplayUtils:
    lcd = None
    scrollSpeed = 0.3
    pauseTime = 2.0


    def __init__(self, lcd):
        self.lcd = lcd





    def backAndForth(self, line1, line2, repeat):

        # max scrolling length is longest line
        maxLength = 0
        if len(line1) > len(line2):
            maxLength = len(line1)
        else:
            maxLength = len(line2)

        # no larger than 32 chars
        if maxLength > 32:
            # display first 16 chars of each maximum of 32
            self.lcd.message(line1[:32] + '\n')
            self.lcd.message(line2[:32])
            maxLength = 32  # adjust as we have just changed the maximum length
        else:
            self.lcd.message(line1 + '\n')
            self.lcd.message(line2)


        # scroll both directions 'repeat' number of times
        for i in range(repeat):
            if maxLength > 16:

                time.sleep(self.pauseTime)  # small pause before moving

                # move lcd text all the way left
                for i in range(maxLength - 16):
                    time.sleep(self.scrollSpeed)
                    self.lcd.move_left()

                time.sleep(self.pauseTime)  # small pause before moving back

                # move lcd text back to original position
                for i in range(maxLength - 16):
                    time.sleep(self.scrollSpeed)
                    self.lcd.move_right()

                time.sleep(self.pauseTime)  # small pause before moving
            else:
                time.sleep(self.pauseTime ** 3)