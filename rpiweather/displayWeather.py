import pywapi
import string
import time
__author__ = 'mike'


class DisplayWeather:
    lcd = None
    noaa_result = pywapi.get_weather_from_noaa('KOWD')

    def __init__(self, lcd):
        DisplayWeather.lcd = lcd

    def run(self, seconds):
        DisplayWeather.lcd.clear()
        print(DisplayWeather.noaa_result)
        DisplayWeather.lcd.message(string.lower(DisplayWeather.noaa_result['temp_c']) + ' C')
        time.sleep(seconds)


