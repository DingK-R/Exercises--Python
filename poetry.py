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

class Poetry_pick():

    def run(self):
        l = self._words()
        BANDS = l[0]
        BEER_BRANDS = l[1]
        PLACES = l[2]
        GOOD_THINGS = l[3]
        EXPRESSIONS = l[4]
        EMOTICONS = l[5]

        saying = """
        Someone just put on {0}. {1}. That's just what it's like at this {2}.
        Feels like {3}.{4}. {5}
        """.format(
            self.pick(BANDS),
            self.pick(BEER_BRANDS),
            self.pick(PLACES),
            self.pick(GOOD_THINGS),
            self.pick(EXPRESSIONS),
            self.pick(EMOTICONS))

        print(saying)

    def pick(self, l):
        return random.choice(l)

    def _words(self):
        BANDS = [
            "Dave Matthews Band",
            "Erykah Badu",
            "Joni Mitchell",
            "Cat Stevens",
            "Guster",
            "Dispatch",
            "early Phil Collins",
            "Ben Folds",
            "Sam Cooke",
            "Carole King"
        ]
        PLACES = [
            "fern bar",
            "swim-up bar",
            "park",
            "big park",
            "regional music event",
            "free local music event",
            "low-cost local music event",
            "beer tasting event",
            "friend's bbq",
            "lazy river"
            ]
        EMOTICONS = [";)"]
        EXPRESSIONS = [
            "bingo",
            "tubular",
            "aw yeah",
            "feels right",
            "emotions just right",
            "everything just right"
            ]
        BEER_BRANDS = [
            "Sierra Nevada",
            "not hoppy IPA",
            "Corona",
            "Corona",
            "Corona"
            ]
        GOOD_THINGS = [
            "hanging with a cool ex",
            "playing pool but not for money",
            "avoiding a nail in the road",
            "meeting Sade",
            "almost meeting Sade",
            "inner-tubing down the Nile with a hippo",
            "reading about Mars and just loving science",
            "snorkeling for the first time",
            "talking to Sade about her trip to Costa Rica",
            "discovering $5 in my pocket and giving it away",
            "an unexpected sunset"
            ]

        return [BANDS, BEER_BRANDS, PLACES, GOOD_THINGS, EXPRESSIONS, EMOTICONS]

Poetry_pick().run()