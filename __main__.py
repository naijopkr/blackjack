""" Main module """
from Classes.Player import Player
from Classes.Round import Round
from utils.constants import PLAYER_TYPES
from utils.utilFunctions import clear

def player_setup():
    """
    Player setup.

    Returns:
        Classes.Player: User's player.

    """
    clear()
    player_name = input('Enter your name: ')
    player_type = PLAYER_TYPES.get('human')
    player = Player(player_name, player_type)
    print(f'Welcome to the game, {player.name}')
    print()
    print(player.bankroll)
    input()

    return player

def start_game():
    """ Starts the game """
    game_on = True
    player = player_setup()

    while game_on:
        if player.bankroll.balance == 0:
            new_deposit = input('You are out of money. Wanna make a new deposit? (YES/no): ')
            if new_deposit.upper() == 'NO':
                break

            player.bankroll.make_deposit()
            clear()

        player_bet = player.bankroll.make_bet()

        game_round = Round(player_bet * 2, player)
        game_round.player_round()
        end_game = game_round.check_burst_blackjack()
        if not end_game:
            game_round.computer_round()
            game_round.showdown()

        game_on = game_round.play_again().upper() != 'NO'
        clear()

if __name__ == '__main__':
    start_game()
