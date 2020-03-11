from Classes.Player import Player
from Classes.Round import Round
from utils.constants import PLAYER_TYPES
from utils.utilFunctions import clear

game_on = True

# Player setup
clear()
player_name = input('Enter your name: ')
player_type = PLAYER_TYPES.get('human')
player = Player(player_name, player_type)
print(player.bankroll)
    
while game_on:
    if (player.bankroll.balance == 0):
        new_deposit = input('You are out of money. Wanna make a new deposit? (YES/no): ')
        if (new_deposit.upper() == 'NO'):
            break

        player.bankroll.make_deposit()
        clear()

    player_bet = player.bankroll.make_bet()

    round = Round(player_bet * 2, player)
    round.player_round()
    end_game = round.check_burst_blackjack()
    if not end_game:
        round.computer_round()
        round.showdown()
    
    game_on = round.play_again().upper() != 'NO'
    clear()
