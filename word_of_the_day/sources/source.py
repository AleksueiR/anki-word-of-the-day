import json
import tempfile
import urllib2
from datetime import datetime

# http://www.dictionary.com/ajax/wotd/2016/4/18/6/0/2016-04-25

# imageUrl = "http://static.sfdict.com/sizedimage/sizedimage?width=455&height=455&url=" + data['2016-04-27']['imageUrl']

# urllib.urlretrieve (imageUrl, "_image.png")

# pprint.pprint(imageUrl)


fileTypes = {
    "application/ogg": ".ogg",
    "audio/basic":	".au",
    "audio/mid":	".mid",
    "audio/mpeg":	".mp3",
    "audio/ogg": ".ogg",
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


class Source(object):

    def __init__(self):
        # User agent string that can be used for requests.
        # At least Google TTS won't give out their translations unless
        # we pretend to be some typical browser.
        self.user_agent = 'Mozilla/5.0'

    def today(self):
        print 'hello'

    def getRawData(self, url):
        """
        Return raw data loaded from an URL and type from the headers.

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

        Wrapper helper function around self.get_data_from_url().
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