import streamlit as st
import art

st.set_page_config(page_title="Auction Program", page_icon="💲")
st.title("Secret Auction Program")
st.code(art.logo)

if "bids" not in st.session_state:
    st.session_state.bids = {}

if "name" not in st.session_state:
    st.session_state.name = ""

if "price" not in st.session_state:
    st.session_state.price = 0.0

name = st.text_input(
    "WHAT IS YOUR NAME?",
    key="name")

price = st.number_input(
    "WHAT IS YOUR BID? $",
    min_value=0.0,
    step=1.0,
    key="price")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("ADD BID"):
        if name.strip():
            st.session_state.bids[name] = price
            st.success(f"Bid added for {name}!")

            st.session_state.name = ""
            st.session_state.price = 0.0
            st.rerun()
        else:
            st.error("Please enter your name.")

with col2:
    if st.button("FINISH AUCTION"):
        if st.session_state.bids:

            highest_bid = max(st.session_state.bids.values())

            winners = [
                bidder
                for bidder, bid in st.session_state.bids.items()
                if bid == highest_bid
            ]

            if len(winners) == 1:
                st.success(
                    f"🏆 The winner is **{winners[0]}** with a bid of **${highest_bid:.2f}**"
                )
            else:
                st.success(
                    f"🏆 It's a tie! Winners: **{', '.join(winners)}** with bids of **${highest_bid:.2f}**"
                )

            st.subheader("All Bids")
            st.write(st.session_state.bids)

        else:
            st.warning("No bids have been entered.")

with col3:
    if st.button("RESET"):
        st.session_state.bids = {}
        st.session_state.name = ""
        st.session_state.price = 0.0
        st.rerun()
