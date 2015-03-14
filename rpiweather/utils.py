__author__ = 'mike'
import threading
import queue

'''
Globally defined variables and functions go here
'''


def init():
    # we need a globally accessible queue
    global lcdQueue
    lcdQueue = queue.Queue()
    global queueLock
    queueLock = threading.Lock()  # queue is not thread safe without this
