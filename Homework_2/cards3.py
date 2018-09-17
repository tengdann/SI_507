import unittest
from operator import itemgetter

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
                
    # Deal out specified number of cards to number of hands
    # If per_hand is -1, deal all cards in deck, regardless if unequal hands
    def deal(self, num_hands, per_hand):
        list_hands = []
        
        for x in range(0, num_hands):
            list_hands.append(Hand([]))
        
        if per_hand != -1:
            for x in range(0, per_hand):
                for hand in list_hands:
                    hand.draw(self)
            
            return list_hands
        else:
            while len(self.cards) != 0:
                for hand in list_hands:
                    try:
                        hand.draw(self)
                    except:
                        pass
            
            return list_hands


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
    
    # Looks through hand, removing pairs of cards (rank, as per poker definition of pair)
    def remove_pairs(self):
        # Time for some recursions
        self.hand.sort(key = for card in self.hand: card.rank_num)
        
        if self.hand[0].rank_num == self.hand[1].rank_num:
            self.remove_card(hand[0])
            self.remove_card(hand[0])
        
        
        
        
class TestEC2(unittest.TestCase):
    def test_deal(self):
        deck = Deck()
        
        # Test simple deal
        test_list = deck.deal(num_hands = 3, per_hand = 5)
        self.assertEqual(len(test_list), 3)
        for hands in test_list:
            self.assertEqual(len(hands.hand), 5)
            
        deck2 = Deck()
            
        # Test per_hand = -1
        test_list2 = deck2.deal(num_hands = 5, per_hand = -1)
        self.assertEqual(len(test_list2), 5)
        for hands2 in test_list2:
            # Should have at least 10 cards per deck
            self.assertTrue(len(hands2.hand) >= 10)
            
        # Testing to see if first hand2 and last hand2 size are different
        self.assertTrue(len(test_list2[0].hand) > len(test_list2[4].hand))
        
    def test_remove_pairs(self):
        hand = Hand([Card(rank = 2), Card(suit = 1, rank = 2), Card(rank = 3), Card(suit = 1, rank = 3)])
        hand.remove_pairs()
        
        # Test pair of rank in hand
        self.assertEqual(len(hand.hand), 2)
        self.assertEqual(str(hand.hand[0]), str(Card(rank = 3)))
        self.assertEqual(str(hand.hand[1]), str(Card(suit = 1, rank = 3)))
        
        # Test three of a rank in hand
        hand2 = Hand([Card(rank = 2), Card(suit = 1, rank = 2), Card(suit = 2, rank = 2), Card(rank = 3), Card(suit = 1, rank = 3)])
        hand2.remove_pairs()
        self.assertEqual(len(hand2.hand), 3)
        self.assertEqual(str(hand2.hand[0]), str(Card(suit = 2, rank = 2)))
        self.assertEqual(str(hand2.hand[1]), str(Card(rank = 3)))
        self.assertEqual(str(hand2.hand[2]), str(Card(suit = 1, rank = 3)))
        

        
if __name__ == "__main__":
    unittest.main(verbosity=2)