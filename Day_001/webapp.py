import streamlit as st

st.set_page_config(page_title="Band Name Generator", page_icon="🎵")
st.title("Welcome to the Band Name Generator!")
city = st.text_input("🏙️ Wich city did you grow up in?\n")
pet = st.text_input("🐱 What is your pet's name? If you don't have one, what name would you give it?\n")

if st.button("GENERATE NAME"):
    # Remove espaços vazios
    city = city.strip()
    pet = pet.strip()

    if city == "" or pet == "":
        st.error("Please fill in all fields!")
    else:
        st.success("Your band name could be: " + city + " " + pet)

