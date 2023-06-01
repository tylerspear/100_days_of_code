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
    player = draw(deck, 2)
    dealer_total = sum(dealer)
    player_total = sum(player)
    if dealer_total == 21:
        print('Blackjack! Dealer wins')
    else:
        if player_total == 21:
            print('Blackjack! Player wins')
        
        while player_total < 21:
            print(f"Dealer's 1st card: {dealer[0]}")
            print(f"Your Cards: {player}, Total: {player_total}")
            hit = input('Would you like another card? (y/n): ')
            if hit == 'y':
                player.append(draw(deck, 1)[0])
                player_total = sum(player)
                # if player goes over 21 and has an ACE, change it to a 1
                if player_total > 21 and 11 in player:
                    player[player.index(11)] = 1
                    player_total = sum(player)
                    print(f"Your Cards: {player}, Total: {player_total}")
                if player_total > 21:
                    print(f"Your Cards: {player}, Total: {player_total}")
                    print('Bust!')
                if player_total == 21:
                    print(f"Your Cards: {player}, Total: {player_total}")
                    print('Blackjack!')
            else:
                #pc keeps drawing until over 16
                
                #compare scores

                # print final scores

                #play again

        




user_choice = input("Would you like to play a game of Blackjack? Type 'y' for yes or 'n' for no. ")

if user_choice == 'y':
    blackjack()
else:
    print("No problem, see you later!")