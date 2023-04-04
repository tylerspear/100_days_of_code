import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
comp_choice = random.randint(0,2)

print("You chose: ")
print(choices[choice])
print("Computer chose: ")
print(choices[comp_choice])

if choice == 0 and comp_choice == 2:
    print("You win with Rock")
elif choice == 0 and comp_choice == 1:
    print("Computer wins with Paper")
elif choice == 1 and comp_choice == 2:
    print("You win with Paper")
else:
    print("It's a tie!")
