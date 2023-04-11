import random
# from words import words
from art import stages


guesses = len(stages) - 1

word_list = ["ardvark", "baboon", "camel"]

#randomly choose a word from the list
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

display = []

for char in chosen_word:
        display.append('_')

game_over = False

while not game_over:
    
    player_guess = input("Guess a letter: ").lower()

    if player_guess not in chosen_word:
         print(stages[guesses])
         guesses -= 1
         
         if guesses == -1:
            print("You lose! Better luck next time")
            print((f'The word was {chosen_word}'))
            game_over = True
            break 

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == player_guess:
            display[i] = player_guess
        
    # if the 2 words match, you win
    if ''.join(display) == chosen_word:
        print("Winner!")
        game_over = True
        print(''.join(display))
        break

    #other wise keep going
    else:
        print(display)
    

