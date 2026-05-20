import streamlit as st

st.title("Welcome to the Band name Generator!")
city = st.text_input("Wich city did you grow up in?\n")
pet = st.text_input("What is your pet's name? If you don't have one, what name would you give it?\n")

if st.button("Generate Name"):
    # Remove espaços vazios
    city = city.strip()
    pet = pet.strip()

    if city == "" or pet == "":
        st.error("Please fill in all fields!")
    else:
        st.success("Your band name could be: " + city + " " + pet)
