#!/usr/bin/env python3

import random

"""
The poet
Write a beautiful poem.
"""


class Poetry():

    def run(self):
        for i in range(0, len(self._words())):
            print(self._verse())

    def _verse(self):
        verse = []
        for n in range(0, 4):
            line = self._words()[n]
            key = random.randint(0, len(line) - 1)
            verse.append(line[key])
        return ' '.join(str(n) for n in verse)

    def _words(self):
        article = ['a', 'the', 'another']
        theme = ['cat', 'dog', 'man', 'woman', 'boy', 'horse']
        verbs = ['sang', 'ran', 'jumped', 'hoped', 'laughed']
        adverbial = ['loudly', 'quietly', 'well', 'badly', 'rudely']

        return [article, theme, verbs, adverbial]

Poetry().run()