class Hand():

    def __init__(self, cards):
        self.cards = cards

    def get_value(self):
        """ Get the value of the hand """
        hand_sum = 0
        total_aces = 0
        for card in self.cards:
            hand_sum += card.value
            if card.value == 11:
                total_aces += 1

        if total_aces > 0:
            for _i in range(total_aces):
                if hand_sum > 21:
                    hand_sum = hand_sum - 10
                else:
                    break

        return hand_sum

    def __str__(self):
        return str(self.get_value())

    def add_card(self, card):
        """ Adds card to hand """

        self.cards.append(card)
