__author__ = 'mike'
# get the current connected ip address

import threading
import socket
import fcntl
import struct
import time
import utils
import message


class DisplayInfo(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    @staticmethod
    def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

    def run(self):
        while True:
            try:
                ip_string = self.get_ip_address('wlan0')
            except IOError:

                # failover to eth0
                try:
                    ip_string = self.get_ip_address('eth0')
                except IOError:
                    ip_string = ''

            # results
            if ip_string == '':
                # no connections found
                utils.queueLock.acquire()
                lcdQueueMessage = message.Message(self.threadID, 'No Connections')
                utils.lcdQueue.enqueue(lcdQueueMessage)
                utils.queueLock.release()
            else:
                # found a connection
                utils.queueLock.acquire()
                lcdQueueMessage = message.Message(self.threadID, ip_string)
                utils.lcdQueue.enqueue(lcdQueueMessage)
                utils.queueLock.release()

            time.sleep(10)
