import json
import pprint
import re
import string
from datetime import datetime

from ..wotd import Wotd
from .source import Source


class DictionaryComSource(Source):
    def __init__(self):
        Source.__init__(self)

        self.base_image_url = u'http://static.sfdict.com/sizedimage/sizedimage?width=455&height=455&url={0}'
        self.base_url = u'http://www.dictionary.com/ajax/wotd/{0}'

    @property
    def today(self):
        today_url_suffix = datetime.now().strftime('%Y/%m/%d')
        today_entry_key = datetime.now().strftime('%Y-%m-%d')
        entry_url = self.base_url.format(today_url_suffix)
        entry_data, file_type = self.getRawData(entry_url)

        # convert to json
        entryDataJson = json.loads(entry_data)[today_entry_key]

        # pprint.pprint(entryDataJson)

        word = entryDataJson[u'word']
        definition = string.join(entryDataJson[u'definitions'], '\\n')
        transcription = entryDataJson[u'pronunciation']

        audio_re = re.compile("""(src|href)=["'](?P<audio>.+?)["']""", flags=re.IGNORECASE)
        audio_urls = audio_re.findall(entryDataJson[u'audioPlayerHtml'])

        # audio_url = u'http://static.sfdict.com/staticrep/dictaudio/M04/M0409900.mp3'
        audio_url = audio_urls[0][1]
        audio_path = self.getTempFile(audio_url)

        print audio_url

        # u'https://avatars1.githubusercontent.com/u/2285779?v=3&s=460'
        image_url = entryDataJson['imageUrl']
        image_path = self.getTempFile(self.base_image_url.format(image_url))

        # print imageFilePath

        return Wotd(word, definition, transcription, audio_path, image_path)
