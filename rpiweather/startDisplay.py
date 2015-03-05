#!/usr/bin/python
from operator import pos

__author__ = 'mike'

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
#from displayTime import display_time
import time
from time import strftime
from displayWeather import DisplayWeather
from displayInfo import DisplayInfo
import thread


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

# Turn on LEDs
led1ON = True
led2ON = True
GPIO.output(led1, led1ON)
GPIO.output(led2, led2ON)


### TIME THREAD ###
displayTimeLocked = True

def display_time(lcd):
    lcd.clear()
    while True:
        print "time"
        if not displayTimeLocked:
            lcd.home()
            lcd.message(strftime("%H:%M:%S") + '\n' + strftime("%Y-%m-%d"))

### IP THREAD ###
displayInfoLocked = False

def get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

def display_ip(lcd):
    while True:
        try:
            ip_string = ''
            print self.get_ip_address('wlan0')
            ip_string = self.get_ip_address('wlan0')
        except IOError:
            ip_string = ''
            print 'no such device: wlan0'

            # failover
            try:
                print "ip: " + self.get_ip_address('eth0')
                ip_string = self.get_ip_address('eth0')
            except IOError:
                ip_string = ''
                print 'no such device: eth0'

        # print results
        if ip_string == '':
            lcd.message('No Connection')
        else:
            if(displayInfoLocked):
                lcd.message('ip: ' + self.ip_string)



# start threads with the same lcd reference.
thread.start_new_thread(display_time,(lcd,))
thread.start_new_thread(display_ip,(lcd,))

## DRIVER THREAD ##
while True:
    if GPIO.event_detected(btn2):
        lcd.clear()
        print "invert"
        displayTimeLocked = not displayTimeLocked
        displayInfoLocked = not displayInfoLocked







