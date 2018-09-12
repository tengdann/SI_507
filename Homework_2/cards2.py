import cards_space
import unittest

class Hand(object):

    # create the Hand with an initial set of cards
	# param: a list of cards
    def __init__(self, init_cards):
        self.hand = init_cards

	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
    def add_card(self, card):
        if card not in self.hand:
            self.hand.append(card)

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand
    def remove_card(self, card):
        if card in self.hand:
            return self.hand.pop(self.hand.index(card))
        else:
            return None

	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
    def draw(self, deck):
        self.addcard(deck.pop_card())
        
        
class TestHand(unittest.TestCase):
    def test_hand_create(self):
        test_hand = [Card(), Card(rank = 3), Card(rank = 4), Card(rank = 5)]
        _hand = Hand(test_hand)
        self.assertEqual(len(_hand.hand), 4)
        self.assertEqual(_hand.hand, test_hand)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)