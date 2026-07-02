import streamlit as st
import art

st.set_page_config(page_title="Secret Auction Program", page_icon="💲")
st.title("Secret Auction Program")
st.code(art.logo)

if "bids" not in st.session_state:
    st.session_state.bids = {}

name = st.text_input("What is your name?")
price = st.number_input("What is your bid? $", min_value=0.0, step=1.0)

col1, col2 = st.columns(2)

with col1:
    if st.button("ADD BID"):
        if name:
            st.session_state.bids[name] = price
            st.success(f"Bid added for {name}!")
        else:
            st.error("Please enter your name.")

with col2:
    if st.button("FINISH AUCTION"):
        if st.session_state.bids:
            winner = max(st.session_state.bids, key=st.session_state.bids.get)
            highest_bid = st.session_state.bids[winner]

            st.success(
                f"🏆 The winner is **{winner}** with a bid of **${highest_bid:.2f}**"
            )

            st.subheader("All Bids")
            st.write(st.session_state.bids)
        else:
            st.warning("No bids have been entered.")
