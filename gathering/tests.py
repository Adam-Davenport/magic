from django.test import TestCase
import json
import requests


# Create your tests here.
class JSON_Tests(TestCase):

    def test_json(self):
        cards = json.load(requests.get('https://api.deckbrew.com/mtg/cards'))
        print(cards)


def test_json():
    cards = requests.get('https://api.deckbrew.com/mtg/cards?page=99999999')
    for c in cards:
        print(c)


if __name__ == '__main__':
    test_json()