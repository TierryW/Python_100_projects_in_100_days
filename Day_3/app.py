print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')

choise1 = input("\n You arrive at a mysterious island."
                "\n There are two paths ahead.\n"
                "Do you go LEFT or RIGHT?\n").lower()

if choise1 == "left":
    
    choise2 = input("\n You reach a dark lake with mist floating above the water."
                    "\n There is a small abandoned boat nearby.\n"
                    "Do you WAIT for welp or SWIN across?\n").lower()
    if choise2 == "wait":
        
        choise3 = input("\n A ghostly boatman silently takes tou to the other side."
                        "\n You arrivve at an ancient temple with 3 glowing doors.\n"
                        "Wich door do you choose? RED, BLUE or YELLOW?\n").lower()
        
        if choise3 == "yellow":
            print("\n Inside the yellow room you find mountains of gold and jewels!\n"
                "YOU FOUND THE TREASURE! YOU WIN!")
        
        elif choise3 == "red":
            print("\n As soon as you enter, flames burst from t he walls.\n"
                "\n You are burned alive.\n"
                "Game Over.")
        
        elif choise3 == "blue":
            print("\n Hungry beasts emerge from the darkness and attack you...\n"
                "Game Over.")
        
        else:
            print("\n Invalid Option!\n"
                "Game Over.")
    
    elif choise2 == "swin":
        print("\n Something movves beneath the water...\n"
            "Game Over.")
    
    else:
        print("\n Invalid Option!\n"
            "Game Over.")

elif choise1 == "right":
    print("\n You fall into a hidden hole covered with leaves.\n"
        "Game Over.")

else:
    print("\n Invalid Option!\n"
        "Game Over.")
