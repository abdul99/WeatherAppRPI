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
        self.lcd = lcd
        self.lcdUtils = DisplayUtils(lcd)

    def run(self):
        self.lcd.clear()

        # request NOAA weather data
        noaa_result = pywapi.get_weather_from_noaa('KOWD')
        print(noaa_result)

        ## PAGE 1
        # pull out string that I want
        if 'weather' in noaa_result:
            weather_string = string.lower(noaa_result['weather'])
        else:
            weather_string = 'n/a'

        if 'temperature_string' in noaa_result:
            temp_string = string.lower(noaa_result['temperature_string'])
        else:
            temp_string = 'n/a'

        # use my util class to display nicely
        self.lcdUtils.backAndForth(weather_string, temp_string, 2)

        self.lcd.clear()

        ## PAGE 2
        # pull out more data
        if 'wind_string' in noaa_result:
            wind_string = string.lower('wind: ' + noaa_result['wind_string'])
        else:
            # fallback
            if 'wind_mph' and 'wind_dir' in noaa_result:
                wind_string = string.lower(
                    'wind: ' + noaa_result['wind_dir'] + " at " + noaa_result['wind_mph'] + ' mph')
            else:
                wind_string = 'n/a'

        if 'windchill_string' in noaa_result:
            windchill_string = string.lower('wchill: ' + noaa_result['windchill_string'])
        else:
            # fallback
            if 'dewpoint_string' in noaa_result:
                windchill_string = string.lower('dewpnt: ' + noaa_result['dewpoint_string'])
            else:
                windchill_string = 'n/a'

        self.lcdUtils.backAndForth(wind_string, windchill_string, 2)


# sample JSON return from noaa_result
# {'weather': u'Light Snow Freezing Fog', 'windchill_c': u'-8', 'ob_url': u'http://www.weather.gov/data/METAR/KOWD.1.txt',
# 'windchill_f': u'17', 'pressure_mb': u'1004.6', 'dewpoint_string': u'19.9 F (-6.7 C)',
# 'suggested_pickup_period': u'60', 'dewpoint_f': u'19.9', 'location': u'Norwood, Norwood Memorial Airport, MA',
# 'dewpoint_c': u'-6.7', 'latitude': u'42.19083', 'wind_mph': u'4.6', 'temp_f': u'23.0', 'temp_c': u'-5.0',
# 'pressure_string': u'1004.6 mb', 'windchill_string': u'17 F (-8 C)', 'station_id': u'KOWD',
# 'wind_string': u'East at 4.6 MPH (4 KT)', 'pressure_in': u'29.66', 'temperature_string': u'23.0 F (-5.0 C)',
# 'two_day_history_url': u'http://www.weather.gov/data/obhistory/KOWD.html', 'wind_dir': u'East', 'wind_degrees': u'70',
# 'observation_time': u'Last Updated on Feb 14 2015, 4:53 pm EST', 'longitude': u'-71.17389',
# 'suggested_pickup': u'15 minutes after the hour', 'relative_humidity': u'88',
# 'observation_time_rfc822': u'Sat, 14 Feb 2015 16:53:00 -0500'}

# {'icon_url_name': u'sn.png', 'weather': u'Light Snow Fog/Mist',
# 'ob_url': u'http://www.weather.gov/data/METAR/KOWD.1.txt', 'pressure_mb': u'1002.2',
# 'dewpoint_string': u'21.9 F (-5.6 C)', 'suggested_pickup_period': u'60', 'dewpoint_f': u'21.9',
# 'location': u'Norwood, Norwood Memorial Airport, MA', 'dewpoint_c': u'-5.6', 'latitude': u'42.19083',
# 'wind_mph': u'0.0', 'temp_f': u'24.0', 'temp_c': u'-4.4', 'pressure_string': u'1002.2 mb', 'station_id': u'KOWD',
#  'wind_string': u'Calm', 'pressure_in': u'29.59', 'temperature_string': u'24.0 F (-4.4 C)',
#  'two_day_history_url': u'http://www.weather.gov/data/obhistory/KOWD.html', 'wind_dir': u'North', 'wind_degrees': u'0',
#  'icon_url_base': u'http://forecast.weather.gov/images/wtf/small/',
#  'observation_time': u'Last Updated on Feb 14 2015, 6:53 pm EST', 'longitude': u'-71.17389',
#  'suggested_pickup': u'15 minutes after the hour', 'relative_humidity': u'91',
#  'observation_time_rfc822': u'Sat, 14 Feb 2015 18:53:00 -0500'}
