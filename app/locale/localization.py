import ConfigParser

__author__ = 'Davor Obilinovic'


class Localization:
    def __init__(self):
        self.parser = ConfigParser.RawConfigParser()
        self.parser.read("locales.loc")

    def get(self, lang, lbl):
        return self.parser.get(lang, lbl)


loc = Localization()