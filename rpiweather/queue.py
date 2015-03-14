__author__ = 'mike'

import utils
'''
A simple FIFO queue for messages to the LCD
'''


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)
