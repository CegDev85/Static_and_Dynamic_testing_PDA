

import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spade", 5)
        self.cards = [self.card1, self.card2]
    

    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self,self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self,self.card1,self.card2))


    def test_total_of_cards(self):
        self.assertEqual("You have a total of 6", CardGame.cards_total(self, self.cards))