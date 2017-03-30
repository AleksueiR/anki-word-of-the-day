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

    word_list = [word.encode('utf-8') for word in word_list]

    description_list = [fetch_desc.get_description(word) for word in word_list[0:3]]

    with open('some.csv', 'w') as f:
        writer = csv.writer(f)

        [short_desc_list, long_desc_list] = zip(*description_list)

        rows = zip(word_list[0:3], short_desc_list[0:3], long_desc_list[0:3])

        writer.writerows(rows)

        print(rows)




do_stuff()
