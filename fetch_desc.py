
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

    true_word = match.group("word").lower()

    print('getting ' + true_word, end='')

    request = requests.get(url.format(true_word))
    page = request.text

    soup = BeautifulSoup(page, 'html.parser')

    shortd = soup.find("p", class_="short")
    longd = soup.find("p", class_="long")

    if not shortd and not longd:
        print(' ---> ✕', end='')
        return ['', '']

    print(' ---> ✔', end='')
    # print(shortd.prettify())
    # print(longd.prettify())

    return [bytes.decode(shortd.encode_contents()), bytes.decode(longd.encode_contents())]

    #return [shortd.prettify().strip().replace('\n', ''), longd.prettify().strip().replace('\n', '')]
