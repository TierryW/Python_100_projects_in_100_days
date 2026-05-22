import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️")
st.title("🏝️ Treasure Island!")
st.subheader("Your mission is to find the treasure.")
st.text(r'''
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

choise1 = st.selectbox("\n You arrive at a mysterious island."
                "\n There are two paths ahead.\n",
                ["Select an Option", "Left", "Right"])

if choise1 == "Left":
    st.text("\n You reach a dark lake with mist floating above the water."
            "\n There is a small abandoned boat nearby.\n")
    
    choise2 = st.selectbox("Do you WAIT for welp or SWIN across?",
            ["Select an Option", "Wait", "Swin"])
    if choise2 == "Wait":
        st.text(r'''
                \n A ghostly boatman silently takes tou to the other side.
                \n You arrivve at an ancient temple with 3 glowing doors.\n
                🔴 RED      🔵 BLUE      🟡 YELLOW
                ''')

        choise3 = st.selectbox("Wich door do you choose?",
                ["Select an Option", "Red", "Blue", "Yellow"])
        
        if choise3 == "yellow":
            st.success("\n Inside the yellow room you find mountains of gold and jewels!\n"
                "YOU FOUND THE TREASURE! YOU WIN!")
            st.balloons()
        
        elif choise3 == "red":
            st.text("\n As soon as you enter, flames burst from t he walls.")
            st.error("\n You are burned alive.\n"
                "Game Over.")
            
        elif choise3 == "blue":
            st.text("\n Hungry beasts emerge from the darkness and attack you...")
            st.error("\n Game Over.")
    
    elif choise2 == "Swin":
        st.text("\n Something movves beneath the water...")
        st.error("\nGame Over.")

elif choise1 == "Right":
    st.text("\n You fall into a hidden hole covered with leaves.")
    st.error("\n Game Over.")
