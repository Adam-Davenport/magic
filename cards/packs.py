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


def get_mythic_count():
    # Bell curve random mythics
    rand = randint(0, 100)
    if rand < 30:
        count = 4
    elif rand < 60:
        count = 5
    elif rand < 75:
        count = 3
    elif rand < 90:
        count = 6
    else:
        count = 7
    return count


def booster_box(set_name):
    box_set = get_set(set_name)
    if box_set.mythics is not none:
        mythic_count = get_mythic_count()
    else:
        mythic_count = 0
