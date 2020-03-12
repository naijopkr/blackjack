from classes.hand import Hand
from classes.bankroll import Bankroll

class Player():

    def __init__(self, name, player_type):
        self.name = name
        self.player_type = player_type
        self.bankroll = Bankroll(self, 500)
        self.status = 0
        self.hand = None

    def init_hand(self, cards):
        """ Initilizes hand """

        self.hand = Hand(cards)

    def show_hand(self, show_down=False):
        """ Shows cards in hand """

        if self.player_type == 0 or show_down:
            for card in self.hand.cards:
                print(f'{card.name} {card.suit}')
        else:
            dealer_card = self.hand.cards[0]
            print(f'{dealer_card.name} {dealer_card.suit}')

    def add_card(self, card):
        """ Adds card to hand """

        self.hand.add_card(card)

    def get_score(self):
        """ Gets hand score """

        return self.hand.get_value()

    def check_status(self):
        """
        Check player status

        Blackjack: 1
        Bust: -1
        Other: 0
        """

        score = self.get_score()
        if score > 21:
            self.status = -1
        elif score == 21:
            self.status = 1
        else:
            self.status = 0
