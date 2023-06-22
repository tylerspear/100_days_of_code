from random import randrange

def draw(deck, num_cards):
    cards = []
    for i in range(num_cards):
        cards.append(deck[randrange(len(deck))])
    return cards


def blackjack():
    game_over = False
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
        
        while player_total < 21 and not game_over:
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
            
            elif hit == 'n':
                while dealer_total <= 16:
                #pc keeps drawing until over 16
                    dealer.append(draw(deck, 1)[0])
                    dealer_total = sum(dealer)
                #compare scores
                if dealer_total > 21 and 11 in dealer:
                    dealer[dealer.index(11)] = 1
                    dealer_total = sum(dealer)
                if dealer_total > 21:
                    print("Dealer Busts!")
                    print("You win")
                    game_over = True

                # print final scores
                if player_total > dealer_total:
                    print("You win!")
                    print(f"Your Cards: {player}, Total: {player_total}")
                    game_over = True
                elif dealer_total > player_total and dealer_total < 21:
                    print("Dealer Wins!")
                    print(f"Dealer Cards: {dealer}, Total: {dealer_total}")
                    game_over = True
    
    play_again = input("Play again?: (y/n): ")
    
    if play_again == 'y':
        blackjack()


user_choice = input("Would you like to play a game of Blackjack? Type 'y' for yes or 'n' for no. ")

if user_choice == 'y':
    blackjack()
else:
    print("No problem, see you later!")