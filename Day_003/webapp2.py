import streamlit as st

st.set_page_config(page_title="Treasure Island 2", page_icon="🏝️")

if "scene" not in st.session_state:
    st.session_state.scene = "start"

st.title("🏝️ Treasure Island 2!")

if st.session_state.scene == "start":
    st.markdown("### Your mission is to find the treasure.")
    st.markdown("### You arrive at a mysterious island during a stormy night.")
    st.markdown("### Two paths appear in front of you...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ GO LEFT"):
            st.session_state.scene = "lake"
            st.rerun()
    
    with col2:
        if st.button("➡️ GO RIGHT"):
            st.session_state.scene = "hole"
            st.rerun()

elif st.session_state.scene == "lake":
    st.markdown("### You reach a dark lake with mist floating above the water.")     
    st.markdown("### There is a small abandoned boat nearby...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏊 SWIN"):
            st.session_state.scene = 'trout'
            st.rerun()
    
    with col2:
        if st.button("⏳ WAIT"):
            st.session_state.scene = "temple"
            st.rerun()

elif st.session_state.scene == "temple":
    st.markdown("### A ghostly boatman silently takes tou to the other side.")
    st.markdown("### You arrivve at an ancient temple with 3 glowing doors...")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔴 RED DOOR"):
            st.session_state.scene = "fire"
            st.rerun()
    
    with col2:
        if st.button("🔵 BLUE DOOR"):
            st.session_state.scene = "beasts"
            st.rerun()

    with col3:
        if st.button("🟡 YELLOW DOOR"):
            st.session_state.scene = "treasure"
            st.rerun()

elif st.session_state.scene == "hole":
    st.markdown("### You fall into a hidden hole covered with leaves...")
    st.markdown("### 💀 GAME OVER")

    if st.button("🔄 RESTART"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "trout":
    st.markdown("### Something moves beneath the water...")
    st.markdown("### 💀 GAME OVER")

    if st.button("🔄 RESTART"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "fire":
    st.markdown("### As soon as you step through the red door...")
    st.markdown("### 🔥 Flames erupt from the walls and floor. You are burned alive.")
    st.markdown("### 💀 Game Over")
    if st.button("🔄 RESTART"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "beasts":
    st.markdown("### As soon as you step through the blue door...")
    st.markdown("### 🐺 Hungry beasts emerge from the darkness and attack you.")
    st.markdown("### 💀 GAME OVER")
    if st.button("🔄 RESTART"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "treasure":
    st.markdown("### Inside the yellow room you find mountains of gold and jewels...")
    st.markdown("### 💰 YOU FOUND THE TREASURE!")
    st.balloons()
    st.markdown("### You Win!")
    st.markdown("### Good luck getting off that island!")
    if st.button("🔄 PLAY AGAIN"):
        st.session_state.scene = "start"
        st.rerun()
