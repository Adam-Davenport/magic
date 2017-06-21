from cards.models import Card
from random import randint, shuffle
from math import floor


class Set():

    def __init__(self, mythics, rares, uncommons, commons):
        self.mythics = mythics
        self.rares = rares
        self.uncommons = uncommons
        self.commons = commons


def get_set(set_name):
    cards = Card.objects.filter(set=set_name)
    mythics = []
    rares = []
    uncommons = []
    commons = []
    for card in cards:
        if card.rarity == 'Mythic Rare':
            mythics.append(card)
        elif card.rarity == 'Rare':
            rares.append(card)
        elif card.rarity == 'Uncommon':
            uncommons.append(card)
        elif card.rarity == 'Common':
            commons.append(card)
    return Set(mythics, rares, uncommons, commons)


def booster_pack(set_name):
    return 'pack'


def booster_box(set_name):
    # Bell curve random mythics
    random_count
    for i in range(6):
        random_count += randint(1, 5)
    mythic_count = 2 + floor(random_count)

