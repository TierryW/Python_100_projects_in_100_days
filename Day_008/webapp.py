import streamlit as st
import logo_ceasar_cipher

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'
    ]

st.set_page_config(page_title="Ceasar Cipher", page_icon="📜")
st.title("CEASAR CIPHER")
st.code(logo_ceasar_cipher.logo)

def ceasar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
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

if "scene" not in st.session_state:
    st.session_state.scene = "encode"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("ENCODE"):
        st.session_state.scene = "encode"

with col2:
    if st.button("DECODE"):
        st.session_state.scene = "decode"

with col3:
    if st.button("RESET"):
        st.session_state.clear()
        st.rerun()

st.write(f"Current mode: **{st.session_state.scene}**")

text = st.text_input("Type your message:")
shift = st.number_input("Type the shift number:", min_value=0, step=1)

if st.button("CIPHER"):
    if text.strip() == "":
        st.warning("Please enter a message.")
    else:
        result = ceasar(text.lower(), shift, st.session_state.scene)
        st.success(f"Here is the {st.session_state.scene}d message:")
        st.code(result)
