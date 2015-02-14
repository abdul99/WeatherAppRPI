import pywapi
import string
import time

__author__ = 'mike'


class DisplayWeather:
    lcd = None

    def __init__(self, lcd):
        DisplayWeather.lcd = lcd

    def run(self, seconds):
        DisplayWeather.lcd.clear()
        noaa_result = pywapi.get_weather_from_noaa('KOWD')
        print(noaa_result)
        # Only print the first 16 chars of each string
        DisplayWeather.lcd.message(string.lower(noaa_result['weather'])[:16]+'\n')
        DisplayWeather.lcd.message(string.lower(noaa_result['temperature_string'])[:16])
        time.sleep(seconds)

# sample JSON return from noaa_result
# {'weather': u'Light Snow Freezing Fog', 'windchill_c': u'-8', 'ob_url': u'http://www.weather.gov/data/METAR/KOWD.1.txt',
# 'windchill_f': u'17', 'pressure_mb': u'1004.6', 'dewpoint_string': u'19.9 F (-6.7 C)',
# 'suggested_pickup_period': u'60', 'dewpoint_f': u'19.9', 'location': u'Norwood, Norwood Memorial Airport, MA',
# 'dewpoint_c': u'-6.7', 'latitude': u'42.19083', 'wind_mph': u'4.6', 'temp_f': u'23.0', 'temp_c': u'-5.0',
# 'pressure_string': u'1004.6 mb', 'windchill_string': u'17 F (-8 C)', 'station_id': u'KOWD',
#  'wind_string': u'East at 4.6 MPH (4 KT)', 'pressure_in': u'29.66', 'temperature_string': u'23.0 F (-5.0 C)',
#  'two_day_history_url': u'http://www.weather.gov/data/obhistory/KOWD.html', 'wind_dir': u'East', 'wind_degrees': u'70',
#  'observation_time': u'Last Updated on Feb 14 2015, 4:53 pm EST', 'longitude': u'-71.17389',
#  'suggested_pickup': u'15 minutes after the hour', 'relative_humidity': u'88',
#  'observation_time_rfc822': u'Sat, 14 Feb 2015 16:53:00 -0500'}

