import streamlit as st
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.markdown("### I'm thinking of a number between **1 and 100**.")

# Inicializa o estado do jogo
if "answer" not in st.session_state:
    st.session_state.answer = randint(1, 100)

if "turns" not in st.session_state:
    st.session_state.turns = 0

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = ""


# Escolha da dificuldade
difficulty = st.radio(
    "CHOOSE A DIFFUCULTY:",
    ["EASY", "HARD"],
    horizontal=True
)

# Botão para iniciar o jogo
if not st.session_state.game_started:

    if st.button("▶️ START GAME"):

        if difficulty == "EASY":
            st.session_state.turns = EASY_LEVEL_TURNS
        else:
            st.session_state.turns = HARD_LEVEL_TURNS

        st.session_state.answer = randint(1, 100)
        st.session_state.game_started = True
        st.session_state.game_over = False
        st.session_state.message = ""

        st.rerun()


# Jogo
if st.session_state.game_started:

    st.divider()

    st.write(
        f"### You have {st.session_state.turns} "
        "attempts remaining."
    )

    guess = st.number_input(
        "MAKE A GUESS:",
        min_value=1,
        max_value=100,
        step=1,
        value=50
    )

    if st.button("🎯 GUESS"):

        if guess > st.session_state.answer:

            st.session_state.message = "🔺 Too high."
            st.session_state.turns -= 1

        elif guess < st.session_state.answer:

            st.session_state.message = "🔻 Too low."
            st.session_state.turns -= 1

        else:

            st.session_state.message = (
                f"🎉 You got it! "
                f"The answer was {st.session_state.answer}."
            )

            st.session_state.game_over = True


        # Verifica se acabou as tentativas
        if st.session_state.turns == 0 and not st.session_state.game_over:

            st.session_state.message = (
                f"💀 You've run out of guesses. "
                f"The answer was {st.session_state.answer}."
            )

            st.session_state.game_over = True


    # Exibe o resultado do palpite
    if st.session_state.message:

        if st.session_state.game_over:

            if "You got it" in st.session_state.message:
                st.success(st.session_state.message)
            else:
                st.error(st.session_state.message)

        elif "Too high" in st.session_state.message:
            st.warning(st.session_state.message)

        elif "Too low" in st.session_state.message:
            st.info(st.session_state.message)


    # Jogo terminado
    if st.session_state.game_over:

        st.divider()

        if st.button("🔄 RESTART"):

            st.session_state.answer = randint(1, 100)
            st.session_state.turns = 0
            st.session_state.game_started = False
            st.session_state.game_over = False
            st.session_state.message = ""

            st.rerun()
