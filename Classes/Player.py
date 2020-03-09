from Classes.Hand import Hand

class Player():

    def __init__(self, name, playerType, cards):
        self.name = name
        self.playerType = playerType
        self.hand = Hand(cards)
        self.status = 0

    def show_hand(self, show_down = False):
        if self.playerType == 0 or show_down:
            for card in self.hand.cards:
                print(card)
        else:
            print(self.hand.cards[0])


    def add_card(self, card):
        self.hand.add_card(card)

    def get_score(self):
        return self.hand.get_value()

    def check_status(self):
        score = self.get_score()
        if (score > 21):
            self.status = -1
        elif (score == 21):
            self.status = 1
