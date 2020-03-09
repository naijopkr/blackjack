class Hand():
    
    def __init__(self, cards):
        self.cards = cards

    def get_value(self):
        sum = 0
        for card in self.cards:
            sum += card.value

        return sum

    def __str__(self):
        return str(self.get_value())

    def add_card(self, card):
        self.cards.append(card)