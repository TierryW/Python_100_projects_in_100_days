import streamlit as st
import logo_ceasar_cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z' ]

st.set_page_config(page_title="Caesar Cipher", page_icon="📜")

st.title("CAESAR CIPHER")
st.code(logo_ceasar_cipher.logo)

def ceasar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "DECODE":
        shift_amount *= -1

    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter)
            shifted_position += shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter

    return cipher_text

# Escolha da operação
direction = st.radio(
    "CHOOSE AN OPTION:",
    ["ENCODE", "DECODE"],
    horizontal=True
)

text = st.text_input("TYPE YOUR MESSAGE:")

shift = st.number_input(
    "TYPE THE SHIFT NUMBER:",
    min_value=1,
    step=1
)

if st.button("RUN CIPHER"):
    result = ceasar(text.lower(), shift, direction)

    st.success(f"HERE IS THE {direction}D RESULT:")
    st.code(result)

if st.button("RESET"):
    st.rerun()
