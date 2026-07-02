import streamlit as st
import json
import os

st.title("🏆 Reveal Winner")

if os.path.exists("bids.json"):
    with open("bids.json", "r") as f:
        bids = json.load(f)

    if bids:
        if st.button("Reveal Winner"):
            winner = max(bids, key=bids.get)
            st.success(f"The winner is {winner} with a bid of ${bids[winner]:.2f}")
    else:
        st.warning("There are no bids.")
else:
    st.warning("There are no bids.")
