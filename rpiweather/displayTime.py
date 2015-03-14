__author__ = 'mike'
# Display the current time to the lcd for the given number of seconds
import threading
import time
from time import strftime
import utils
import message


class DisplayTime(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            utils.queueLock.acquire()
            text = strftime("%H:%M:%S") + '\n' + strftime("%Y-%m-%d")
            lcdQueueMessage = message.Message(self.threadID, text)
            utils.lcdQueue.enqueue(lcdQueueMessage)
            utils.queueLock.release()
            time.sleep(0.1)





