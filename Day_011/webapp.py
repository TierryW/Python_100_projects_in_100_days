import streamlit as st
from game import deal_card, start_game, calculate_score, compare, dealer_turn
from cards import CARD_ART, BLANKCARD

st.set_page_config(page_title="Blackjack", page_icon="♠️", layout="wide")

if "game" not in st.session_state:
    st.session_state.game = start_game()

def draw_hand(cards, hidden=False):
    arts = []

    for i, card in enumerate(cards):
        art = BLANKCARD if hidden and i == 1 else CARD_ART[card["rank"]]
        arts.append(art.splitlines())

    linhas = [" ".join(linha) for linha in zip(*arts)]
    st.code("\n".join(linhas), language=None)

game = st.session_state.game

user_cards = game["user_cards"]
computer_cards = game["computer_cards"]
game_over = game["game_over"]

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

st.title("🃏 Blackjack")

dealer_col, player_col = st.columns(2)

with dealer_col:
    st.subheader("Dealer")
    draw_hand(computer_cards, hidden=not game_over)

    if game_over:
        if computer_score == 0:
            st.write("### Score: Blackjack")
        else:
            st.write(f"### Score: {computer_score}")
    else:
        st.write("### Score: ?")

with player_col:
    st.subheader("Player")
    draw_hand(user_cards)

    if user_score == 0:
        st.write("### Score: Blackjack")
    else:
        st.write(f"### Score: {user_score}")

st.divider()

_, col1, col2, col3, _ = st.columns([1, 2, 2, 2, 1])

with col1:
    if not game_over:
        if st.button("🃏 HIT", use_container_width=True):
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)

            if user_score == 0 or user_score > 21:
                game["game_over"] = True
            st.rerun()

with col2:
    if not game_over:
        if st.button("✋ STAND", use_container_width=True):
            dealer_turn(computer_cards)
            game["game_over"] = True
            st.rerun()

with col3:
    if st.button("🔄 RESTART", use_container_width=True):
        st.session_state.game = start_game()
        st.rerun()

game_over = game["game_over"]
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if game_over:
    st.divider()
    st.header("Result")
    st.success(compare(user_score, computer_score))
