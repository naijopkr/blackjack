from Classes.Deck import Deck

test_deck = Deck()

test_deck.shuffle()

print(len(test_deck))
cards = test_deck.draw_card(4)
print(cards)
print(test_deck)
print(len(test_deck))