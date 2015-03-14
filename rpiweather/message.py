__author__ = 'mike'


class Message():
    def __init__(self, id, message):
        self.id = id
        self.message = message

    def getMessage(self):
        return self.message

    def getId(self):
        return self.id
