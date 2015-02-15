__author__ = 'mike'

import socket
import fcntl
import struct
import time


class DisplayInfo:
    lcd = None

    def __init__(self, lcd):
        DisplayInfo.lcd = lcd

    def get_ip_address(self,ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

    def run(self, seconds):
        print self.get_ip_address('wlan0')
        print self.get_ip_address('eth0')
        # time.sleep(seconds)
