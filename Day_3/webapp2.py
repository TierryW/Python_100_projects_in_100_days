import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️")

if "scene" not in st.session_state:
    st.session_state.scene = "start"

st.title("🏝️ Treasure Island!")

if st.session_state.scene == "start":
    st.markdown("### Your mission is to find the treasure.")
    st.markdown("### You arrive at a mysterious island during a stormy night.\n")
    st.markdown("### Two paths appear in front of you...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Go Left"):
            st.session_state.scene = "lake"
            st.rerun()
    
    with col2:
        if st.button("➡️ Go Right"):
            st.session_state.scene = "hole"
            st.rerun()

elif st.session_state.scene == "lake":
    st.write("""
            You reach a dark lake with mist floating above the water.
            
            There is a small abandoned boat nearby...
            """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏳ Wait"):
            st.session_state.scene = "temple"
            st.rerun()

    with col2:
        if st.button("🏊 Swim"):
            st.session_state.scene = 'trout'
            st.rerun()

elif st.session_state.scene == "temple":
    st.write("""
            A ghostly boatman silently takes tou to the other side.
            
            You arrivve at an ancient temple with 3 glowing doors...
            """)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔴 Red Door"):
            st.session_state.scene = "fire"
            st.rerun()
    
    with col2:
        if st.button("🔵 Blue Door"):
            st.session_state.scene = "beasts"
            st.rerun()

    with col3:
        if st.button("🟡 Yellow Door"):
            st.session_state.scene = "treasure"
            st.rerun()

elif st.session_state.scene == "hole":
    st.error("You fall into a hidden hole covered with leaves...")
    st.markdown("### 💀 Game Over")

    if st.button("🔄 Restart"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "trout":
    st.error("Something moves beneath the water...")
    st.markdown("### 💀 Game Over")

    if st.button("🔄 Restart"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "fire":
    st.error("🔥 As soon as you enter, flames burst from t he walls. You are burned alive...")
    st.markdown("### 💀 Game Over")
    if st.button("🔄 Restart"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "beasts":
    st.error("🐺 Hungry beasts emerge from the darkness and attack you...")
    st.markdown("### 💀 Game Over")
    if st.button("🔄 Restart"):
        st.session_state.scene = "start"
        st.rerun()

elif st.session_state.scene == "treasure":
    st.success("Inside the yellow room you find mountains of gold and jewels!")
    st.success("💰 YOU FOUND THE TREASURE!")
    st.balloons()
    st.markdown("### 🎉 You Win!")
    if st.button("🔄 Play Again"):
        st.session_state.scene = "start"
        st.rerun()
