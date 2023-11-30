#import the data object
from data import data
import random

print("Welcome to the Higher/Lower Game")
print("The object of the game is to guess which of the 2 pop culture names was searched more times.")
print("Try to get as many correct in a row as you can. If you get one wrong, the game is over")
print("Good luck!")

def new_game():
    score = 0
    game_over = False

    while not game_over:
        term1 = data[random.randint(0,len(data)-1)]
        term2 = data[random.randint(0,len(data)-1)]
        if term2["name"] == term1["name"]:
            term2 = data[random.randint(0,len(data)-1)]

        highest = "a" if term1["follower_count"] > term2["follower_count"] else "b"

        print(f'A: Name: {term1["name"]}, Description: {term1["description"]}')
        print(f'B: Name: {term2["name"]}, Description: {term2["description"]}')

        selection = input("A or B?: ").lower()
        
        if selection == highest:
            print("Correct!")
            score += 1
            print(f"Score {score}")
        else:
            print("Sorry, that's incorrect")
            print(f"Final Score: {score}")
            game_over = True        

new_game()

play_again = input("Would you like to play again? (Y/N): ")
if play_again == "Y":
    new_game()

    
