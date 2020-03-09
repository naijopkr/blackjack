from Classes.Deck import Deck
from Classes.Player import Player
from utils.constants import PLAYER_TYPES
from utils.utilFunctions import clear

deck = Deck()

deck.shuffle()

player_name = input('Enter your name: ')
player_type = PLAYER_TYPES.get('human')
player_cards = deck.draw_card(2)
player = Player(player_name, player_type, player_cards)

dealer = Player(
    'Dealer', 
    PLAYER_TYPES.get('computer'), 
    deck.draw_card(2)
)

while(True):
    clear()
    print('YOUR CARDS:')
    player.show_hand()

    print('\n\nDEALER CARDS:')
    dealer.show_hand()

    hit = input('\n\nDo you want another card? (YES/no)')

    if (hit.upper() == 'NO'):
        break

    player.add_card(deck.draw_card(1).pop())
    player.check_status()
    
    if (player.status != 0):
        break

if (player.status == 1):
    print('BLACKJACK!!! YOU WIN!!')
    input()
elif (player.status == -1):
    print('BURST!!! YOU LOST!!')
    input()
else:
    while (dealer.get_score() < 21):
        if (dealer.get_score() > player.get_score()):
            break
        else:
            dealer.add_card(deck.draw_card(1).pop())

clear()
print('END GAME\n\n')
print(player.name)
player.show_hand()
print(f'SCORE: {player.get_score()}\n\n')

print(dealer.name)
dealer.show_hand(True)
print(f'SCORE: {dealer.get_score()}\n\n')


if (dealer.get_score() > 21 or player.get_score() >= dealer.get_score()):
    print('YOU WIN!!')
else:
    print('YOU LOST!!')