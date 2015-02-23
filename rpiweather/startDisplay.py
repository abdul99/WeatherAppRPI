#!/usr/bin/python
from operator import pos

__author__ = 'mike'

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
from displayTime import DisplayTime
from displayWeather import DisplayWeather
from displayInfo import DisplayInfo


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

# p5 header pins on the rpi
led1 = 29
led2 = 28
btn1 = 30
btn2 = 31
# LEDS are OUTPUTS
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

# BTNS are INPUTS. they are setup to pull down
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setup RISING edge listeners (button released)
GPIO.add_event_detect(btn1, GPIO.RISING, bouncetime=200)
GPIO.add_event_detect(btn2, GPIO.RISING, bouncetime=200)

# GPIO.output(led1,True) ## turn on by default
# GPIO.output(led2,True)


# Display objects
view_time = DisplayTime(lcd)
view_weather = DisplayWeather(lcd)
view_info = DisplayInfo(lcd)

led1ON = True
led2ON = True
GPIO.output(led1, led1ON)
GPIO.output(led2, led2ON)

back = False
fwrd = False
# This pages through the different screen info pages
options = {0 : view_time.run(1),
           1 : view_weather.run(),
           2 : view_info.run(1)}
position = 0 #default starting position
while True:

    if GPIO.event_detected(btn1):
        position = position - 1
        if position < 0:
            position = 2

    if GPIO.event_detected(btn2):
        position = position + 1
        if position > 2:
            position = 0

    options[position]()

    # view_time.run(10)
    # view_weather.run()
    # view_info.run(10)






