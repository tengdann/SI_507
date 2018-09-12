import unittest

# Because what even is importing from another file
class Card(object):
    suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
    rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

    def __init__(self, suit=0,rank=2):
        self.suit = self.suit_names[suit]
        if rank in self.faces: # self.rank handles printed representation
            self.rank = self.faces[rank]
        else:
            self.rank = rank
        
        self.rank_num = rank # To handle winning comparison

    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

class Deck(object):
    def __init__(self): # Don't need any input to create a deck of cards
        # This working depends on Card class existing above
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order

    def __str__(self):
        total = []
        for card in self.cards:
            total.append(card.__str__())
        # shows up in whatever order the cards are in
        return "\n".join(total) # returns a multi-line string listing each card

    def pop_card(self, i=-1):
        # removes and returns a card from the Deck
        # default is the last card in the Deck
        return self.cards.pop(i) # this card is no longer in the deck -- taken off

    def shuffle(self):
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def sort_cards(self):
        # Basically, remake the deck in a sorted way
        # This is assuming you cannot have more than the normal 52 cars in a deck
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

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
        self.add_card(deck.pop_card())
        
        
class TestHand(unittest.TestCase):
    def test_hand_create(self):
        test_hand = [Card(), Card(rank = 3), Card(rank = 4), Card(rank = 5)]
        _hand = Hand(test_hand)
        self.assertEqual(len(_hand.hand), 4)
        self.assertEqual(_hand.hand, test_hand)
        
    def test_add_remove(self):
        card = Card()
        card2 = Card(rank = 3)
        card3 = Card(rank = 4)
        card4 = Card(rank = 5)
                
        test_hand = [card, card2, card3, card4]
        _hand = Hand(test_hand)
        
        # Testing removing a card in hand
        rm_card = _hand.remove_card(card2)
        corr_rm_card = Card(rank = 3)
        self.assertEqual(len(_hand.hand), 3)
        self.assertEqual(str(rm_card), str(corr_rm_card))
        
        # Testing removing a card not in hand; should do nothing to hand
        rm_card2 = _hand.remove_card(card2)
        corr_rm_card = None
        self.assertEqual(len(_hand.hand), 3)
        self.assertEqual(rm_card2, corr_rm_card)
        
        # Testing adding back a card not in hand
        _hand.add_card(card2)
        self.assertEqual(len(_hand.hand), 4)
        self.assertTrue(card2 in _hand.hand)
        
        # Testing adding back a card already in hand; should do nothing
        _hand.add_card(card3)
        self.assertEqual(len(_hand.hand), 4)
        self.assertEqual(_hand.hand.count(card3), 1)
        
    def test_draw(self):
        _hand = Hand([])
        deck = Deck()
        
        _hand.draw(deck)
        
        # Should be one card in hand
        self.assertEqual(len(_hand.hand), 1)
        
        # Should be 51 cards in deck (52 - 1)
        self.assertEqual(len(deck.cards), 51)
        
        
if __name__ == "__main__":
    unittest.main(verbosity=2)