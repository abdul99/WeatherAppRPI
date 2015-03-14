#!/usr/bin/python
__author__ = 'mike'

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time
import utils
import displayTime
import displayInfo
import displayWeather

# Initalize global variables only once
utils.init()

# Raspberry Pi pin configuration:
lcd_rs = 22  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en = 27
lcd_d4 = 17
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Initialize LEDs and buttons
# MUST USE BCM SCHEME FOR P5 HEADER
GPIO.setmode(GPIO.BCM)

# p5 header pins on the rpi (buttons and leds)
led1 = 29
led2 = 28
btn1 = 31
btn2 = 30

# LEDS are OUTPUTS
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

# Turn on LEDs
led1ON = True
led2ON = True
GPIO.output(led1, led1ON)
GPIO.output(led2, led2ON)

# BTNS are INPUTS. they are setup to pull down
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setup RISING edge listeners (button released)
GPIO.add_event_detect(btn1, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(btn2, GPIO.RISING, bouncetime=200)

# Create threads
timeThread = displayTime.DisplayTime(1, "TimeThread")
ipThread = displayInfo.DisplayInfo(2, "IpThread")
weatherThread = displayWeather.DisplayWeather(3, "WeatherThread")

# Start threads
timeThread.start()
ipThread.start()
weatherThread.start()

### Consumer thread ###
messageList = ["", "", "", ""]  # cant index an empty array
currentThread = 1


def updateDisplay(message):
    messageList[message.id - 1] = message.message


while True:
    utils.queueLock.acquire()
    dequeueMessage = utils.lcdQueue.dequeue()
    utils.queueLock.release()
    if dequeueMessage != None:
        # update the array of messages to track slower threads
        updateDisplay(dequeueMessage)

        # display what we have
        lcd.home()
        if currentThread == 3:
            # workaround for multi line display
            # TODO: this needs a real fix
            lines = messageList[currentThread - 1].split(',',1) # split at first ,
            lcd.message(lines[0]+'\n'+lines[1])
        else:
            lcd.message(messageList[currentThread - 1])

    if GPIO.event_detected(btn1):
        lcd.clear()
        # print "switching screens"
        currentThread += 1
        if currentThread > 3:
            currentThread = 1