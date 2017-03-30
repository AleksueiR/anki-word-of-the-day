
import re

import requests
from bs4 import BeautifulSoup


def get_description(word):
    url = "https://www.vocabulary.com/dictionary/definition.ajax?search={0}&lang=en"
    regex = r"^(?P<word>.*?)( \d\.)?$"

    #note = mw.reviewer.card.note()
    #word = note["Word"]

    match = re.search(regex, word)
    if not match:
        return

    request = requests.get(url.format(match.group("word")))
    page = request.text

    soup = BeautifulSoup(page, 'html.parser')

    shortd = soup.find("p", class_="short")
    longd = soup.find("p", class_="long")

    if not shortd and not longd:
        print('no descriptions')
        return ['', '']

    # print(shortd.prettify())
    # print(longd.prettify())

    return [shortd.prettify().strip(), longd.prettify().strip()]
