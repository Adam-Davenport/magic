from django.test import TestCase
from cards.packs import Booster_Pack, Create_Battle_Pack, Booster_Box, get_set


# Create your tests here.
class BoosterTest(TestCase):
    def setUp(self):
        current_set = 'AVR'
        self.booster = Booster_Pack(current_set)
        test_set = get_set('AVR')
        print(len(test_set.commons))
        # print(len(box.set.commons))

    def test_battle_pack(self):
        print('test')
        # Create_Battle_Pack(self.booster)
