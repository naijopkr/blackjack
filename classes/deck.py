import random
from utils.constants import VALUES, DECK_SUITS

CARDS = VALUES.keys()
SUITS = DECK_SUITS.keys()

class Deck():

    def __init__(self):
        self.deck_template = set()
        for suit in SUITS:
            for card in CARDS:
                new_card = {
                    "suit": DECK_SUITS.get(suit),
                    "name": card,
                    "value": VALUES.get(card),
                }
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
        """ Shuffled deck set """

        shuffled_deck = []
        i = 0
        while i < len(self.deck_template):
            new_index = random.randint(0, len(self.deck) - 1)
            card = self.deck.pop(new_index)
            shuffled_deck.append(card)
            i += 1

        self.deck = shuffled_deck

    def draw_card(self, how_many):
        """
        Draw cards from deck

        Arguments:
        int: Number of cards to draw from deck
        """
        if len(self.deck) == 0:
            self.__init__()
            self.shuffle()

        cards = []
        for _ in range(how_many):
            cards.append(self.deck.pop())

        return cards
