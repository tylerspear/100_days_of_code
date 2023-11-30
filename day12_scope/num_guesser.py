import random
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 5
secret_num = random.randint(1,100)

if diff == "easy" :
    attempts = 7

while attempts > 0:
    print(f"You have {attempts} attempt(s) remaining.")
    guess = int(input("Make a guess: "))
    if guess == secret_num:
        print("You win!")
        break
    elif guess > secret_num:
        print("Too high")
    else:
        print("Too low")

    attempts -= 1

if attempts <= 0:
    print("Sorry, you're out of attempts")

print(f"The secret number was: {secret_num}")