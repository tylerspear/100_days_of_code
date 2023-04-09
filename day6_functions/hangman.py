import random
word_list = ["ardvark", "baboon", "camel"]

#randomly choose a word from the list
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

#ask for user to guess a letter
player_guess = input("Guess a letter: ").lower()

display = []

for char in chosen_word:
    display.append('_')

for i in range(0, len(chosen_word)-1):
    if chosen_word[i] == player_guess:
        display[i] = player_guess       
print(display)

