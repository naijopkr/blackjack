from Classes.Card import Card
from Classes.Player import Player
from utils.constants import PLAYER_TYPES

suits = ['hearts', 'diamonds', 'spades', 'clubs']
cards = []
for i in range(4):
    card = Card(suits[i], 'ace')
    cards.append(card)

other_card = Card('hearts', 'king')
cards.append(other_card)

player = Player('Testing', PLAYER_TYPES.get('human'), cards)
score = player.get_score()
player.show_hand()
print(score)
