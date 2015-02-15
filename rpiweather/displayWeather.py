from numpy.core.tests.test_numerictypes import test_create_values_nested_multiple
import pywapi
import string
import time
from displayUtils import DisplayUtils

__author__ = 'mike'


class DisplayWeather:
    lcd = None
    lcdUtils = None

    def __init__(self, lcd):
        DisplayWeather.lcd = lcd
        DisplayWeather.lcdUtils = DisplayUtils(lcd)

    def run(self):
        DisplayWeather.lcd.clear()

        # request NOAA weather data
        noaa_result = pywapi.get_weather_from_noaa('KOWD')
        print(noaa_result)

        ## PAGE 1
        # pull out string that I want
        weather_string = string.lower(noaa_result['weather']) + '\n'
        temp_string = string.lower(noaa_result['temperature_string'])

        # use my util class to display nicely
        DisplayWeather.lcdUtils.backAndForth(weather_string,temp_string,3)


        # # display first 16 chars of each
        # DisplayWeather.lcd.message(weather_string)
        # DisplayWeather.lcd.message(temp_string)
        #
        # maxLength = 0
        # if len(weather_string) > len(temp_string):
        #     maxLength = len(weather_string)
        # else:
        #     maxLength = len(temp_string)
        #
        # # scroll both directions 3 times
        # for i in range(3):
        #     if maxLength > 16:
        #         time.sleep(2.0)  # small pause before moving
        #         # move lcd text all the way left
        #         for i in range((maxLength - 16) - 1):
        #             time.sleep(0.7)
        #             DisplayWeather.lcd.move_left()
        #         time.sleep(1.0)  # small pause before moving back
        #         # move lcd text back to original position
        #         for i in range((maxLength - 16) - 1):
        #             time.sleep(0.7)
        #             DisplayWeather.lcd.move_right()





# sample JSON return from noaa_result
# {'weather': u'Light Snow Freezing Fog', 'windchill_c': u'-8', 'ob_url': u'http://www.weather.gov/data/METAR/KOWD.1.txt',
# 'windchill_f': u'17', 'pressure_mb': u'1004.6', 'dewpoint_string': u'19.9 F (-6.7 C)',
# 'suggested_pickup_period': u'60', 'dewpoint_f': u'19.9', 'location': u'Norwood, Norwood Memorial Airport, MA',
# 'dewpoint_c': u'-6.7', 'latitude': u'42.19083', 'wind_mph': u'4.6', 'temp_f': u'23.0', 'temp_c': u'-5.0',
# 'pressure_string': u'1004.6 mb', 'windchill_string': u'17 F (-8 C)', 'station_id': u'KOWD',
# 'wind_string': u'East at 4.6 MPH (4 KT)', 'pressure_in': u'29.66', 'temperature_string': u'23.0 F (-5.0 C)',
#  'two_day_history_url': u'http://www.weather.gov/data/obhistory/KOWD.html', 'wind_dir': u'East', 'wind_degrees': u'70',
#  'observation_time': u'Last Updated on Feb 14 2015, 4:53 pm EST', 'longitude': u'-71.17389',
#  'suggested_pickup': u'15 minutes after the hour', 'relative_humidity': u'88',
#  'observation_time_rfc822': u'Sat, 14 Feb 2015 16:53:00 -0500'}
