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

print("Welcome to Rock Paper Scissors (RPS)")
player_choise = int(input("What do you choose?:\n 0 - Rock \n 1 - Paper \n 2 - Scissors \n"))
computer_choise = random.randint(0, 2)

if player_choise == 0:
    print("You chose:")
    print(rock)

elif player_choise == 1:
    print("You chose:")
    print(paper)

elif player_choise == 2:
    print("You chose:")
    print(scissors)

else:
    print("Error! Choose between 0, 1, or 2.")

if computer_choise == 0:
    print("Computer chose:")
    print(rock)

elif computer_choise == 1:
    print("Computer chose:")
    print(paper)

elif computer_choise == 2:
    print("Computer chose:")
    print(scissors)

if player_choise == 0 and computer_choise == 0:
    print("Draw")

elif player_choise == 0 and computer_choise == 1:
    print("You Lose")

elif player_choise == 0 and computer_choise == 2:
    print("You Win")

elif player_choise == 1 and computer_choise == 1:
    print("Draw")

elif player_choise == 1 and computer_choise == 0:
    print("You Win")

elif player_choise == 1 and computer_choise == 2:
    print("You Lose")

elif player_choise == 2 and computer_choise == 2:
    print("Draw")

elif player_choise == 2 and computer_choise == 1:
    print("You Win")

elif player_choise == 2 and computer_choise == 0:
    print("You Lose")
