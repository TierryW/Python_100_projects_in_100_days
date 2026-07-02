import random
import streamlit as st

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', 'A', 
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 
        'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '=', '+']

st.set_page_config(page_title="PyPassword Generator", page_icon="🔑")
st.title("🔑 PyPassword Generator")

n_letters = st.number_input("How many letters would you like in your password?", min_value=1, step=1)
n_symmbols = st.number_input("How many symbols would you like?", min_value=1, step=1)
n_numbers = st.number_input("How many numbers would you like?", min_value=1, step=1)

if st.button("GENERATOR"):
    password_list = []
    for char in range(0, n_letters):
        password_list.append(random.choice(letters))

    for char in range(0, n_symmbols):
        password_list.append(random.choice(symbols))

    for char in range(0, n_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    st.text("Your password is: ")
    st.code(password)

