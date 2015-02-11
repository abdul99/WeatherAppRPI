#!/usr/bin/python
__author__ = 'mike'

import Adafruit_CharLCD as LCD
from displayTime import DisplayTime


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

view_time = DisplayTime(lcd)

while True:
    view_time.run(60)

lcd.clear();
