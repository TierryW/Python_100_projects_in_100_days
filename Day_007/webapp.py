import streamlit as st
import random

stages_hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    "PYTHON",
    "STREAMLIT",
    "PROGRAMMING",
    "HANGMAN",
    "KEYBOARD"
]

# Inicialização
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)

if "chosen_letters" not in st.session_state:
    st.session_state.chosen_letters = []

if "lives" not in st.session_state:
    st.session_state.lives = 6

if "game_over" not in st.session_state:
    st.session_state.game_over = False

def restart_game():
    st.session_state.word = random.choice(WORDS)
    st.session_state.chosen_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False

st.title("WELCOME TO THE HANGMAN GAME!!!")

# Desenho da forca
st.code(stages_hangman[6 - st.session_state.lives])

st.write(f"### ❤️ LIVES: {st.session_state.lives}")

# Palavra escondida
display_word = ""

for letter in st.session_state.word:
    if letter in st.session_state.chosen_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

st.markdown(f"## {display_word}")

# Vitória
if "_" not in display_word:
    st.balloons()
    st.success("✔️ YOU WIN!")
    st.session_state.game_over = True

# Teclado
if not st.session_state.game_over:

    keyboard = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    for row in keyboard:
        cols = st.columns(len(row))

        for i, letter in enumerate(row):
            with cols[i]:

                if st.button(
                    letter,
                    key=letter,
                    disabled=letter in st.session_state.chosen_letters,
                    use_container_width=True
                ):

                    st.session_state.chosen_letters.append(letter)

                    if letter not in st.session_state.word:
                        st.session_state.lives -= 1

                    if st.session_state.lives <= 0:
                        st.session_state.game_over = True

                    st.rerun()

# Derrota
if st.session_state.lives <= 0:
    st.error(f"❌ YOU LOSE! THE WORD WAS: \t{st.session_state.word}")

# Letras usadas
st.write("### USED LETTERS:")
st.write(", ".join(st.session_state.chosen_letters))

# Reiniciar
if st.session_state.game_over:
    if st.button("🔄 PLAY AGAIN"):
        restart_game()
        st.rerun()
