class Hand():
    
    def __init__(self, cards):
        self.cards = cards

    def get_value(self):
        sum = 0
        total_aces = 0
        for card in self.cards:
            sum += card.value
            if card.value == 11:
                total_aces += 1

        if total_aces > 0:
            for _i in range(total_aces):
                if sum > 21:
                    sum = sum - 10
                else:
                    break

        return sum

    def __str__(self):
        return str(self.get_value())

    def add_card(self, card):
        self.cards.append(card)