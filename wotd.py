import json
import tempfile
import urllib2
from datetime import datetime

# http://www.dictionary.com/ajax/wotd/2016/4/18/6/0/2016-04-25


# imageUrl = "http://static.sfdict.com/sizedimage/sizedimage?width=455&height=455&url=" + data['2016-04-27']['imageUrl']

# urllib.urlretrieve (imageUrl, "image.png")

# pprint.pprint(imageUrl)


fileTypes = {
    "audio/basic":	".au",
    "audio/mid":	".mid",
    "audio/mpeg":	".mp3",
    "audio/x-aiff":	".aif",
    "audio/x-mpegurl": ".m3u",
    "audio/x-pn-realaudio":	".ra",
    "audio/x-wav":	".wav",

    "image/bmp": ".bmp",
    "image/cis-cod": ".cod",
    "image/gif": ".gif",
    "image/ief": ".ief",
    "image/jpeg": ".jpg",
    "image/pipeg": ".jfif",
    "image/png": ".png",
    "image/svg+xml": ".svg",
    "image/tiff": ".tif",
    "image/x-cmu-raster": ".ras",
    "image/x-cmx": ".cmx",
    "image/x-icon": ".ico"
}

class Wotd(object):

    def __init__(self):
        # User agent string that can be used for requests.
        # At least Google TTS won't give out their translations unless
        # we pretend to be some typical browser.
        self.user_agent = 'Mozilla/5.0'

    def today(self):
        print 'hello'

    def getRawData(self, url):
        """
        Return raw data loaded from an URL.

        Helper function. Put in an URL and it sets the agent, sends
        the requests, checks that we got error code 200 and returns
        the raw data only when everything is OK.
        """

        try:
            # There have been reports that the request was send in a
            # 32-bit encoding (UTF-32?). Avoid that. (The whole things
            # is a bit curious, but there shouldn't really be any harm
            # in this.)
            request = urllib2.Request(url.encode('ascii'))
        except UnicodeDecodeError:
            request = urllib2.Request(url)

        try:
            # dto. But i guess this is even less necessary.
            request.add_header('User-agent', self.user_agent.encode('ascii'))
        except UnicodeDecodeError:
            request.add_header('User-agent', self.user_agent)
        response = urllib2.urlopen(request)

        if 200 != response.code:
            raise ValueError(str(response.code) + ': ' + response.msg)

        return response.read(), response.headers.type

    def getTempFile(self, url, extension = None):
        """
        Download raw data from url and put into a tempfile

        Wrapper helper function aronud self.get_data_from_url().
        """

        data, fileType = self.getRawData(url)

        # Try to guess the file extension if possible.
        if extension is None:
            extension = fileTypes.get(fileType, u'.file')

        # We put the data into RAM first so that we don't have to
        # clean up the temp file when the get does not work. (Bad
        # get_data raises all kinds of exceptions that fly through
        # here.)

        tfile = tempfile.NamedTemporaryFile(
            delete=False, prefix=u'anki_wotd_', suffix=extension)

        tfile.write(data)
        tfile.close()

        return tfile.name


class DictionaryComWotd(Wotd):

    def __init__(self):
        Wotd.__init__(self)

        self.image_prefix = u'http://static.sfdict.com/sizedimage/sizedimage?width=455&height=455&url={0}'
        self.url = u'http://www.dictionary.com/ajax/wotd/{0}'

    def today(self):
        today = datetime.now().strftime('%Y/%m/%d')
        entryUrl = self.url.format(today)
        entryData, type = self.getRawData(entryUrl)

        print json.loads(entryData)

        soundUrl = u'http://static.sfdict.com/staticrep/dictaudio/M04/M0409900.mp3'
        soundFilePath = self.getTempFile(soundUrl)

        print soundFilePath


        imageUrl = u'https://avatars1.githubusercontent.com/u/2285779?v=3&s=460'
        imageFilePath = self.getTempFile(imageUrl)

        print imageFilePath