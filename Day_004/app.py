import random

def rock():
    # Rock
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def paper():
    # Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def scissors():
    # Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def show_choise(choise):
    if choise == 0:
        rock()
    elif choise == 1:
        paper()
    elif choise == 2:
        scissors()

def main():
    print("Welcome to Rock Paper Scissors (RPS)")
    player = int(input("What do you choose?:\n 0 - Rock \n 1 - Paper \n 2 - Scissors \n"))
    
    options = [0, 1, 2]

    if player not in options:
        print("Error! Choose between 0, 1, or 2.")
        return
    
    computer = random.choice(options)
    print("\n You chose: ")
    show_choise(player)

    print("\n Computer chose: ")
    show_choise(computer)

    if player == computer:
        print("It's a draw!")
    
    elif ((player == 0 and computer == 2) or (player == 1 and computer == 0)
        or (player == 2 and computer == 1)):
        print("You win!")
    
    else:
        print("You lose! Computer wins!")

main()
