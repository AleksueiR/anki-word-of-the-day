#!/usr/bin/python3.3

import csv
import os
import re

import fetch_desc

def read_list(name):
    file_list = open(name, 'r')
    word_list = file_list.read().splitlines()

    # print(word_list)

    return word_list

def fetch_def(word):

    print(word)


def do_stuff():
    word_list = read_list('English__Word Vault_2_utf.csv')

    # word_list = [word.encode('utf-8') for word in word_list]

    fromlen = 0
    tolen = len(word_list)
    sep = '<br><br>'

    #description_list = [sep.join(fetch_desc.get_description(word)) for word in word_list[0:tolen]]
    row_generator = ([word, fetch_desc.get_description(word)] for word in word_list[fromlen:tolen])
    row_list = [[word, sep.join(desc)] for [word, desc] in row_generator if ''.join(desc) != ""]

    with open('some.csv', encoding='utf-8', mode='w', newline='') as f:
        writer = csv.writer(f)

        # [short_desc_list, long_desc_list] = zip(*description_list)

        # rows = zip(word_list[0:3], short_desc_list[0:3], long_desc_list[0:3])

        # rows = zip(word_list[fromlen:tolen], description_list[fromlen:tolen])

        # list_rows = list(rows)

        writer.writerows(row_list)

        print(len(row_list), len(word_list), end=" ")


import sys
print (sys.version)
do_stuff()
