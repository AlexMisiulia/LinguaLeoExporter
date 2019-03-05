class Word:
    text = '';
    context = '';

    def __init__(self, text):
        self.text = text

class Base(object):
    data = []

    def __init__(self, source):
        self.source = source

    def get(self):
        return self.data

    def read(self):
        raise NotImplementedError('Not implemented yet')


class Kindle(Base):
    def read(self):
        self.data = "not implemented yet"


class Text(Base):
    def read(self):
        f = open(self.source)
        for word in f.readlines():
            self.data.append(Word(word))
        f.close()