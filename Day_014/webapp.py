import streamlit as st
import random
from game_data import data

st.set_page_config(page_title="Higher or Lower", page_icon="📈")

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def initialize_game():
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.account_a = random.choice(data)

    st.session_state.account_b = random.choice(data)

    while st.session_state.account_a == st.session_state.account_b:
        st.session_state.account_b = random.choice(data)

def next_round(user_guess):
    account_a = st.session_state.account_a
    account_b = st.session_state.account_b

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_followers_count, b_followers_count)

    if is_correct:
        st.session_state.score += 1

        # B passa a ser A na próxima rodada
        st.session_state.account_a = account_b

        # Escolhe uma nova conta B
        st.session_state.account_b = random.choice(data)

        while st.session_state.account_a == st.session_state.account_b:
            st.session_state.account_b = random.choice(data)

        st.session_state.message = (
            f"✅ You're right! Current score: "
            f"{st.session_state.score}"
        )

    else:
        st.session_state.game_over = True

        st.session_state.message = (
            f"❌ Sorry, that's wrong! "
            f"Final score: {st.session_state.score}"
        )

if "score" not in st.session_state:
    initialize_game()

st.title("Higher or Lower")
st.subheader("Who has more followers?")

if not st.session_state.game_over:

    account_a = st.session_state.account_a
    account_b = st.session_state.account_b

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🅰️ Compare A")

        st.write(format_data(account_a))

    with col2:
        st.markdown("### 🅱️ Against B")

        st.write(format_data(account_b))

    st.markdown("---")

    st.markdown("### Who has more followers?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🅰️ A has more", use_container_width=True):
            next_round("a")
            st.rerun()

    with col2:
        if st.button("🅱️ B has more", use_container_width=True):
            next_round("b")
            st.rerun()

if "message" in st.session_state:
    st.info(st.session_state.message)

st.markdown(f"### 🏆 Score: {st.session_state.score}")

if st.session_state.game_over:

    st.warning("Game Over!")

    if st.button("🔄 Play Again", use_container_width=True):
        initialize_game()

        if "message" in st.session_state:
            del st.session_state.message

        st.rerun()
