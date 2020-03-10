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
    # Make your bets
    while True:
        try:
            player_bet = player.bankroll.bet(
                int(input('Enter the amount you want to bet: '))
            )
        except:
            print('Invalid value for a bet. Try again!')
        else: 
            break

    round = Round(player_bet * 2, player)
    round.player_round()
    end_game = round.check_burst_blackjack()
    if not end_game:
        round.computer_round()
    
    game_on = round.showdown().upper() != 'NO'

    
