import json
import pprint
import urllib
from string import Template
from datetime import datetime

# http://www.dictionary.com/ajax/wotd/2016/4/18/6/0/2016-04-25


# imageUrl = "http://static.sfdict.com/sizedimage/sizedimage?width=455&height=455&url=" + data['2016-04-27']['imageUrl']

# urllib.urlretrieve (imageUrl, "image.png")

# pprint.pprint(imageUrl)


class Wotd:

    def __init__(self):

        return

    def today(self):
        print 'hello'

class DictionaryComWotd(Wotd):

    def __init__(self):
        Wotd.__init__(self)

        self.image_prefix = u'http://static.sfdict.com/sizedimage/sizedimage?width=455&height=455&url='
        self.url = u'http://www.dictionary.com/ajax/wotd/${date}'

    def today(self):
        today = datetime.now().strftime('%Y/%m/%d')

        response = urllib.urlopen(Template(self.url).substitute(date=today))
        data = json.loads(response.read())

        print data