
import re
import urllib2
from bs4 import BeautifulSoup


###

## # import the main window object (mw) from aqt
## from aqt import mw
## # import the "show info" tool from utils.py
## from aqt.utils import showInfo
## # import all of the Qt GUI library
## from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def get_description():
    url = "https://www.vocabulary.com/dictionary/definition.ajax?search={0}&lang=en"

    regex = r"^(?P<word>.*?)( \d\.)?$"

    word = "Barn 2."

    match = re.search(regex, word)
    if not match:
        return

    request = urllib2.Request(url.format(match.group("word")))
    response = urllib2.urlopen(request)

    page = response.read()

    soup = BeautifulSoup(page, 'html.parser')

    shortd = soup.find("p", class_="short")
    longd = soup.find("p", class_="long")

    if not shortd and not longd:
        print('no descriptions')
        return

    print(shortd.prettify())
    print(longd.prettify())

    ## note = mw.reviewer.card.note()
    ## note["Notes"] = shortd.prettify()
    ## note.flush()

## # create a new menu item, "test"
## action = QAction("get_description", mw)
## # set it to call testFunction when it's clicked
## action.triggered.connect(get_description)
## # and add it to the tools menu
## mw.form.menuTools.addAction(action)

get_description()
