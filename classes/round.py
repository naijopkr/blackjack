from classes.deck import Deck
from classes.player import Player

from utils.constants import PLAYER_TYPES
from utils.util_functions import clear

class Round():

    # Deck setup
    deck = Deck()
    deck.shuffle()

    # Dealer setup
    dealer = Player(
        'Dealer',
        PLAYER_TYPES.get('computer'),
    )

    def __init__(self, pot, player):
        self.pot = pot
        self.player = player
        print(len(self.deck))

        self.player.init_hand(self.deck.draw_card(2))
        self.dealer.init_hand(self.deck.draw_card(2))

    def show_hand(self, showdown=False):
        """ Shows player and dealer hands """

        print('YOUR CARDS:')
        self.player.show_hand()
        print(f'SCORE: {self.player.get_score()}')
        print()

        print('DEALER CARDS:')
        self.dealer.show_hand(showdown)
        if showdown:
            print(f'SCORE: {self.dealer.get_score()}')
        print()

    def check_burst_blackjack(self):
        """ Checks player's hand for blackjack or burst """

        if self.player.status == 1:
            clear()
            self.player.bankroll.add_funds(self.pot)
            print('BLACKJACK!!! YOU WIN!!')
            print()
            print('YOUR CARDS:')
            self.player.show_hand(True)
            print(f'SCORE: {self.player.get_score()}')
            print()
            print(self.player.bankroll)
            input()
            return True

        if self.player.status == -1:
            clear()
            print('BURST!!! YOU LOST!!')
            print()
            print('YOUR CARDS:')
            self.player.show_hand(True)
            print(f'SCORE: {self.player.get_score()}')
            print()
            print(self.player.bankroll)
            input()
            return True

        return False

    def showdown(self):
        """ Shows final hands, scores and result (win/lose) """

        clear()
        print('SHOWDOWN')
        self.show_hand(True)

        dealer_burst = self.dealer.get_score() > 21
        dealer_lose = self.player.get_score() >= self.dealer.get_score()

        if dealer_burst or dealer_lose:
            self.player.bankroll.add_funds(self.pot)
            print('YOU WON!')
        else:
            print('YOU LOST!')

        print(self.player.bankroll)

    def player_round(self):
        """ Starts player round """

        while True:
            self.player.check_status()
            if self.player.status != 0:
                break

            clear()
            self.show_hand()

            hit = input('Do you want another card? (YES/no)')

            if hit.upper() == 'NO':
                self.player.check_status()
                break

            self.player.add_card(self.deck.draw_card(1).pop())


    def computer_round(self):
        """ Starts computer round """

        while self.dealer.get_score() < 21:
            clear()
            self.show_hand(True)
            input('Press any key...')

            if self.dealer.get_score() > self.player.get_score():
                break

            self.dealer.add_card(self.deck.draw_card(1).pop())
