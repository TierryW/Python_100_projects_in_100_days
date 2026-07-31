import streamlit as st
from game import deal_card, start_game, calculate_score, compare, dealer_turn
from cards import CARD_ART, BLANKCARD

st.set_page_config(page_title="Blackjack", page_icon="♠️", layout="wide")

st.markdown("""
<style>

.stApp{
    background-color: #0B55D1E;
}

h1,h2,h3{
    text-align:center;
    color:white;
}

[data-testid="stMarkdownContainer"]{
    color:white;
}

</style>
""", unsafe_allow_html=True)

if "game" not in st.session_state:
    st.session_state.game = start_game()

def draw_hand(cards, hidden=False):
    arts = []

    for i, card in enumerate(cards):
        if hidden and i == 1:
            arts.append(BLANKCARD.splitlines())
        else:
            arts.append(CARD_ART[card["rank"]].splitlines())

    linhas = []

    for i in range(len(arts[0])):
        linhas.append("   ".join(card[i] for card in arts))

    st.code("\n".join(linhas))

game = st.session_state.game

user_cards = game["user_cards"]
computer_cards = game["computer_cards"]
game_over = game["game_over"]

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

st.title("🃏 Blackjack")
st.header("Dealer")
draw_hand(computer_cards, hidden=not game_over)

if game_over:
    if computer_score == 0:
        st.subheader("Score: Blackjack")
    else:
        st.subheader(f"Score: {computer_score}")
else:
    st.subheader("Score: ?")

st.divider()

st.header("Player")
draw_hand(user_cards)

if user_score == 0:
    st.subheader("Score: Blackjack")
else:
    st.subheader(f"Score: {user_score}")

st.divider()

col1, col2, col3 = st.columns(3)

# -------------------------
# HIT
# -------------------------

with col1:

    if not game_over:

        if st.button("🃏 Hit", use_container_width=True):
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)

            if user_score == 0 or user_score > 21:
                game["game_over"] = True
            st.rerun()

# -------------------------
# STAND
# -------------------------

with col2:

    if not game_over:

        if st.button("✋ Stand", use_container_width=True):
            dealer_turn(computer_cards)
            game["game_over"] = True
            st.rerun()

# -------------------------
# NEW GAME
# -------------------------

with col3:

    if st.button("🔄 New Game", use_container_width=True):
        st.session_state.game = start_game()
        st.rerun()

game_over = game["game_over"]

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if game_over:
    st.divider()
    st.header("Result")
    st.success(compare(user_score, computer_score))
