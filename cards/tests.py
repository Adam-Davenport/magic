from django.test import TestCase
from cards.packs import get_set


# Create your tests here.
def test_set():
    card_set = get_set('AVR')
    for c in card_set:
        print(c)

if __name__ == '__main__':
    test_set()
