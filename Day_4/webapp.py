import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors (RPS)", page_icon="✊🤚✌️")

rock_art = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = r'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors_art = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
'''

choises = ["ROCK", "PAPER", "SCISSORS"]

if "scene" not in st.session_state:
    st.session_state.scene = "start"

if "player_choice" not in st.session_state:
    st.session_state.player_choice = ""

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""

if st.session_state == "start":
    st.markdown("### Welcome to Rock Paper Scissors (RPS)")
    st.markdown("### What do you choose?")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✊ ROCK"):
            st.session_state.player_choice = "ROCK"
            st.session_state.scene = "result" 
            st.rerun()

    with col2:
        if st.button("🤚 PAPER"):
            st.session_state.player_choice = "PAPER"
            st.session_state.scene = "result" 
            st.rerun()

    with col3:
        if st.button("✌️ SCISSORS"):
            st.session_state.player_choice = "SCISSORS"
            st.session_state.scene = "result" 
            st.rerun()

elif st.session_state.scene == "result":
    st.session_state.computer_choice = random.choice(choises)

    player = st.session_state.player_choice
    computer = st.session_state.computer_choice

    st.markdown("### RESULT")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👤 YOU")
        if player == "ROCK":
            st.code(rock_art)
        
        elif player == "PAPER":
            st.code(paper_art)

        elif player == "SCISSORS":
            st.code(scissors_art)

    with col2:
        st.markdown("### 🤖 COMPUTER")
        if computer == "ROCK":
            st.code(rock_art)
        
        elif computer == "PAPER":
            st.code(paper_art)

        elif computer == "SCISSORS":
            st.code(scissors_art)

    if player == computer:
        st.warning("🤝 IT'S A DRAW!")

    elif ((player == "ROCK" and computer == "SCISSORS") or (player == "PAPER" and computer == "ROCK")
        or (player == "SCISSORS" and computer == "PAPER")):
        st.success("🎉 YOU WIN!")

    else:
        st.error("💀 You lose!")
    
    if st.button("🔄 Play Again"):
        st.session_state.scene = "start"
        st.rerun()
