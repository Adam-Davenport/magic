from django.test import TestCase
from cards.packs import Booster


# Create your tests here.
class BoosterTest(TestCase):
    def setUp(self):
        booster = Booster('LEA', 3)

    def test_battle_pack(self):
        print('test')
