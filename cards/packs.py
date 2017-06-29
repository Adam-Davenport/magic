from cards.models import Card, Battle_Pack, Battle
from random import randint, shuffle
from math import floor


class Set():

    def __init__(self, mythics, rares, uncommons, commons):
        self.mythics = mythics
        self.rares = rares
        self.uncommons = uncommons
        self.commons = commons


class Booster():

    def __init__(self, set_name, amount):
        self.packs = []
        self.set = self.get_set(set_name)
        if amount == 36:
            self.box()
        else:
            self.single(amount)

    # Get all cards in the current set
    def get_set(self, set_name):
        cards = Card.objects.filter(set_name=set_name)
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

    # Generate boosters as though they are singles
    def single(self, amount):
        for i in range(amount):
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
            mythic_chance = randint(1, 7)
            if mythic_chance == 7 and len(self.set.mythics) > 0:
                index = randint(0, len(self.set.mythics)-1)
                mythic = self.set.mythics[index]
                pack.append(mythic)
            else:
                index = randint(0, len(self.set.rares)-1)
                pack.append(self.set.rares[index])
            self.packs.append(pack)

    # Determine how many mythics will be in a booster box
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

    # Generate an entire booster box
    def box(self):
        self.mythic_count = self.get_mythic_count()
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
                index = randint(0, len(self.set.mythics)-1)
                mythic = self.set.mythics[index]
                self.mythic_count -= 1
                pack.append(mythic)
            else:
                index = randint(0, len(self.set.rares)-1)
                pack.append(self.set.rares[index])
            self.packs.append(pack)
        shuffle(self.packs)

    # Create a dec file from the pack with 2 of each lands
    def battle_pack(self):
        # Create temp dec file
        self.battle_packs = []
        self.battle = Battle.objects.create(
            set_name=self.set,
        )
        for pack in self.packs:
            file = open('tempdeckfile.dec', 'w')
            for card in pack:
                file.write('1 {}\n'.format(card.name))
            land = ['Swamp', 'Mountain', 'Plains', 'Forrest', 'Island']
            for l in land:
                file.write('2 {}\n'.format(l))
            file_location = file.name
            file.close()
            # Create record in database
            bp = Battle_Pack.objects.create(
                set_name=self.set,
                battle=self.battle
            )
            bp.save()
            file_name = 'boosterdeck{}.dec'.format(str(bp.pk))
            bp.cards.save(file_name, open(file_location, 'r'))
            bp.save()
            self.battle_packs.append(bp)
