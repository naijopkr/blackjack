from utils.constants import values, suits

class Card():

    def __init__(self, suit, name):
        self.suit = suits.get(suit)
        self.name = name
        self.value = values.get(name)

    def __str__(self):
        return f'{self.name} {self.suit}'
