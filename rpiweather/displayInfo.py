__author__ = 'mike'
# get the current connected ip address and display it to the connected lcd

import socket
import fcntl
import struct
import time


class DisplayInfo:
    lcd = None
    ip_string = ''

    def __init__(self, lcd):
        self.lcd = lcd

    def get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

    def run(self, seconds):
        self.lcd.clear()
        try:
            self.ip_string = ''
            print self.get_ip_address('wlan0')
            self.ip_string = self.get_ip_address('wlan0')
        except IOError:
            self.ip_string = ''
            print 'no such device: wlan0'

            # failover
            try:
                print "ip: " + self.get_ip_address('eth0')
                self.ip_string = self.get_ip_address('eth0')
            except IOError:
                self.ip_string = ''
                print 'no such device: eth0'

        # print results
        if self.ip_string == '':
            self.lcd.message('No Connections')
        else:
            self.lcd.message('ip: ' + self.ip_string)
        time.sleep(seconds)
