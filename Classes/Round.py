from Classes.Deck import Deck
from Classes.Player import Player

from utils.constants import PLAYER_TYPES
from utils.utilFunctions import clear

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

    def show_hand(self, showdown = False):
        clear()
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
        if self.player.status == 1:
            self.player.bankroll.add_funds(self.pot)
            self.show_hand(True)
            print('BLACKJACK!!! YOU WIN!!')
            print()
            print(self.player.bankroll)
            input()
            return True
        elif (self.player.status == -1):
            self.player.show_hand(True)
            print('BURST!!! YOU LOST!!')
            print()
            print(self.player.bankroll)
            input()
            return True

        return False

    def showdown(self):
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
        return input('Wanna play again? (YES/no): ')


    def player_round(self):
        while True:
            self.show_hand()

            hit = input('Do you want another card? (YES/no)')

            if (hit.upper() == 'NO'):
                self.player.check_status()
                break

            self.player.add_card(self.deck.draw_card(1).pop())
            self.player.check_status()
            
            if (self.player.status != 0):
                break


    def computer_round(self):
        while self.dealer.get_score() < 21:
            self.show_hand(True)
            input('Press any key...')

            if (self.dealer.get_score() > self.player.get_score()):
                break
            else:
                self.dealer.add_card(self.deck.draw_card(1).pop())