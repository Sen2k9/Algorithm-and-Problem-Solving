"""
Deck of Cards:
Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.
"""
import random
import unittest


class Cards():
    """
    Cards class contains the implementation of card number and suit
    """

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


class DeckOfCards:
    """
    Generic Deck of Cards
    which includes shuffling cards and drawing cards methods/procedures
    """

    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []

    def shuffle(self):
        for count in range(len(self.cards)):
            change_with = random.randint(count)
            self.cards[count], self.cards[change_with] = self.cards[change_with], self.cards[count]

        return self.cards

    def draw(self):
        return self.cards.pop()


class Blackjack(DeckOfCards):
    """
    Subclass of DeckofCards
    Blackjack implement particular kind of playing cards types
    It has it's own customize method name value
    """

    def value(self):

        value, ace = 0, 0
        for card in self.cards:
            value += min(card.number, 10)
            ace += 1
        while value <= 11:
            if ace:
                value += 10
                ace -= 1
        return value


class TestSuite(unittest.TestCase):
    """
    TestSuite to test all functions
    """

    def test_deck_cards(self):
        decks = DeckOfCards([Cards(5, "Hearts"), Cards(7, "clubs")])
        self.assertEqual(decks.draw().suit, "clubs")

    def test_blackjack_cards(self):
        blackjack = Blackjack([Cards(5, "Hearts"), Cards(7, "clubs")])
        self.assertEqual(blackjack.value(), 12)


if __name__ == '__main__':
    unittest.main()
