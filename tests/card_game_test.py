import unittest
from part_2_code.src.card_game import CardGame
from part_2_code.src.card import Card

class TestCardGame(unittest.TestCase):



    def setUp(self):
        self.card_game = CardGame()


    def test_check_ace(self):
        card = Card("Hearts", 5)
        self.assertEqual(False, self.card_game.check_for_ace(card))

    def test_check_highest_card(self):
        card1 = Card("Hearts", 3)
        card2 = Card("Clubs", 8)
        self.assertEqual(card2, self.card_game.highest_card(card1, card2))

    def test_total(self):
        card1 = Card("Hearts", 3)
        card2 = Card("Clubs", 8)
        cards = [card1, card2]
        self.assertEqual(11, self.card_game.cards_total(cards))