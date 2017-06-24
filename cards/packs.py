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


class Booster_Box():

    def __init__(self, set_name):
        self.set = get_set(set_name)
        self.packs = []
        self.mythic_count = self.get_mythic_count()
        self.assemble_packs()

    def get_mythic_count(self):
        if len(self.set.mythics) > 0:
            rand = randint(0, 100)
            if rand < 30:
                return 4
            elif rand < 60:
                return 5
            elif rand < 75:
                return 3
            elif rand < 90:
                return 6
            else:
                return 7
        else:
            return 0

    def assemble_packs(self):
        for i in range(0, 36):
            pack = []
            # Commons
            for c in range(1, 11):
                index = randint(0, len(self.set.commons)-1)
                pack.append(self.set.commons[index])
            # Uncommons
            for u in range(1, 3):
                index = randint(0, len(self.set.uncommons)-1)
                pack.append(self.set.uncommons[index])
            # Rare
            shuffle(self.set.mythics)
            if self.mythic_count > 0:
                mythic = self.set.mythics[0]
                self.mythic_count -= 1
                pack.append(mythic)
            else:
                index = randint(0, len(self.set.rares)-1)
                pack.append(self.set.rares[index])
            self.packs.append(pack)
        shuffle(self.packs)
