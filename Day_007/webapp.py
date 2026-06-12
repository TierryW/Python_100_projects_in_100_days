import streamlit as st
import random
import string

# Lista de palavras
WORDS = [
    "PYTHON",
    "STREAMLIT",
    "HANGMAN",
    "PROGRAMMING",
    "COMPUTER",
    "KEYBOARD",
    "DEVELOPER",
    "DATABASE"
]

# Inicialização do jogo
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)

if "chosen_letters" not in st.session_state:
    st.session_state.chosen_letters = []

if "lives" not in st.session_state:
    st.session_state.lives = 6

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Função para reiniciar
def restart_game():
    st.session_state.word = random.choice(WORDS)
    st.session_state.chosen_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False

# Título
st.title("🎮 Hangman Game")

# Exibe vidas
st.subheader(f"❤️ Lives: {st.session_state.lives}")

# Monta a palavra exibida
display_word = ""

for letter in st.session_state.word:
    if letter in st.session_state.chosen_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

st.markdown(f"# {display_word}")

# Verifica vitória
if "_" not in display_word:
    st.success("🎉 YOU WIN!")
    st.session_state.game_over = True

# Teclado
if not st.session_state.game_over:

    keyboard = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    st.write("### Choose a letter")

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
if st.session_state.game_over and st.session_state.lives <= 0:
    st.error(f"💀 YOU LOSE! The word was: {st.session_state.word}")

# Botão de reinício
if st.session_state.game_over:
    if st.button("🔄 Play Again"):
        restart_game()
        st.rerun()

# Letras utilizadas
st.write("### Used Letters")
st.write(", ".join(st.session_state.chosen_letters))
