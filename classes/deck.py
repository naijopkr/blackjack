import collections
import random
from utils.constants import VALUES, DECK_SUITS

CARDS = VALUES.keys()
SUITS = DECK_SUITS.keys()

class Deck():

    Card = collections.namedtuple('Card', 'suit name value')

    def __init__(self):
        self.deck_template = set()
        for suit in SUITS:
            for card in CARDS:
                new_card = Deck.Card(
                    suit=DECK_SUITS.get(suit),
                    name=card,
                    value=VALUES.get(card)
                )
                self.deck_template.add(new_card)

        self.deck = list(self.deck_template)

    def __str__(self):
        cards = []
        for card in self.deck:
            cards.append(str(card))

        return str(cards)

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        """ Shuffles deck set """
        random.shuffle(self.deck)

    def draw_card(self, how_many):
        """
        Draw cards from deck

        Arguments:
        int: Number of cards to draw from deck
        """
        cards = []
        for _ in range(how_many):
            if len(self.deck) == 0:
                self.__init__()
                self.shuffle()

            cards.append(self.deck.pop())

        return cards
