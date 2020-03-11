import random
from Classes.Card import Card
from utils.constants import values, suits

cards = values.keys()
suits = suits.keys()

class Deck():

    def __init__(self):
        self.deck_template = set()
        for suit in suits:
            for card in cards:
                self.deck_template.add(Card(suit, card))

        self.deck = list(self.deck_template)

    def __str__(self):
        cards = []
        for card in self.deck:
            cards.append(str(card))

        return str(cards)

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        shuffled_deck = []
        i = 0
        while i < len(self.deck_template):
            new_index = random.randint(0, len(self.deck) - 1)
            card = self.deck.pop(new_index)
            shuffled_deck.append(card)
            i += 1

        self.deck = shuffled_deck
    
    def draw_card(self, how_many):
        if len(self.deck) == 0:
            self.__init__()
            self.shuffle()

        cards = []
        for _ in range(how_many):
            cards.append(self.deck.pop())

        return cards

