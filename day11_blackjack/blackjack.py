from random import randrange
def draw(deck, num_cards):
    cards = []
    for i in range(num_cards):
        cards.append(deck[randrange(len(deck))])
    return cards


def blackjack():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # random 2 cards to dealer and player
    dealer = draw(deck, 2)
    print(dealer)
    # check for blackjack (Ace + 10)

    # if both have blackjack, pc wins

    # if only 1 has blackjack then they win




user_choice = input("Would you like to play a game of Blackjack? Type 'y' for yes or 'n' for no. ")

if user_choice == 'y':
    blackjack()
else:
    print("No problem, see you later!")