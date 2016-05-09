# -*- mode: python ; coding: utf-8 -*-
#
# Copyright © 2016
#
# Based on field_data.py by  Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
# http://www.gnu.org/copyleft/agpl.html

"""
One class to store information for the downloader
"""

from anki.sound import stripSounds
from anki.utils import stripHTML


class FieldData(object):
    def __init__(self, w_field, a_field, word):
        self.word_field_name = w_field
        self.audio_field_name = a_field
        # This is taken from aqt/browser.py.
        self.word = word.replace(u'<br>', u' ')
        self.word = self.word.replace(u'<br />', u' ')
        if strip_interpunct:
            self.word = self.word.replace(u'・', u'')
        self.word = stripHTML(self.word)
        self.word = stripSounds(self.word)
        # Reformat so we have exactly one space between words.
        self.word = u' '.join(self.word.split())

    @property
    def empty(self):
        return not self.word
