import streamlit as st
import art

st.set_page_config(page_title="Auction Program", page_icon="💲")

st.title("Secret Auction Program")
st.code(art.logo)

if "bids" not in st.session_state:
    st.session_state.bids = {}

with st.form(
    "auction_form", clear_on_submit=True):
    name = st.text_input("WHAT IS YOUR NAME?")
    price = st.number_input(
        "WHAT IS YOUR BID? $",
        min_value=0.0,
        step=1.0
    )

    submitted = st.form_submit_button("ADD BID")

    if submitted:
        if name.strip():
            st.session_state.bids[name] = price
            st.success(f"Bid added for {name}!")
        else:
            st.error("Please enter your name.")

col1, col2 = st.columns(2)

with col1:
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
                    f"🏆 The winner is **{winners[0]}** "
                    f"with a bid of **${highest_bid:.2f}**"
                )
            else:
                st.success(
                    f"🏆 It's a tie! Winners: "
                    f"**{', '.join(winners)}** "
                    f"with bids of **${highest_bid:.2f}**"
                )

            st.subheader("All Bids")
            st.write(st.session_state.bids)

        else:
            st.warning("No bids have been entered.")

with col2:
    if st.button("RESET"):
        st.session_state.bids = {}
        st.rerun()
