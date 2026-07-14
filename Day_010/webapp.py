import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Calculator")

if "display" not in st.session_state:
    st.session_state.display = ""

def add_to_display(value):
    st.session_state.display += value

def backspace():
    st.session_state.display = st.session_state.display[:-1]

# Visor
st.text_input("Display", value=st.session_state.display, disabled=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("⌫", use_container_width=True):
        backspace()

with col2:
    if st.button("C", use_container_width=True):
        st.session_state.display = ""

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", use_container_width=True):
        add_to_display("7")

with col2:
    if st.button("8", use_container_width=True):
        add_to_display("8")

with col3:
    if st.button("9", use_container_width=True):
        add_to_display("9")

with col4:
    if st.button("/", use_container_width=True):
        add_to_display("/")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", use_container_width=True):
        add_to_display("4")

with col2:
    if st.button("5", use_container_width=True):
        add_to_display("5")

with col3:
    if st.button("6", use_container_width=True):
        add_to_display("6")

with col4:
    if st.button("*", use_container_width=True):
        add_to_display("*")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", use_container_width=True):
        add_to_display("1")

with col2:
    if st.button("2", use_container_width=True):
        add_to_display("2")

with col3:
    if st.button("3", use_container_width=True):
        add_to_display("3")

with col4:
    if st.button("-", use_container_width=True):
        add_to_display("-")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("0", use_container_width=True):
        add_to_display("0")

with col2:
    if st.button(".", use_container_width=True):
        add_to_display(".")

with col3:
    if st.button("=", use_container_width=True):
        try:
            result = eval(st.session_state.display)
            st.session_state.display = f"{result:.2f}"
        except:
            st.session_state.display = "Error"

with col4:
    if st.button("+", use_container_width=True):
        add_to_display("+")
