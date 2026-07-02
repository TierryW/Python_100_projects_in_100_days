import streamlit as st
import json
import os
import art

st.title("Secret Auction")
st.text(art.logo)

name = st.text_input("What is your name?")
bid = st.number_input("What is your bid?", min_value=0.0, step=1.0)

if st.button("Submit Bid"):
    if name:
        if os.path.exists("bids.json"):
            with open("bids.json", "r") as f:
                bids = json.load(f)
        else:
            bids = {}

        bids[name] = bid

        with open("bids.json", "w") as f:
            json.dump(bids, f)

        st.success("Your bid has been submitted!")
        st.info("Please pass the computer to the next bidder.")
    else:
        st.error("Enter your name.")
