import streamlit as st
import requests

API_START = "http://localhost:8000/start"

def story_setup_screen():
    st.title("🪄 Story Setup")

    # -----------------------------
    # Inputs
    # -----------------------------
    title = st.text_input("Story Title", placeholder="e.g., The Whispering Forest")

    genre = st.selectbox(
        "Genre",
        ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror", "Comedy"]
    )

    initial_hook = st.text_area(
        "Initial Hook / Setting",
        placeholder="Describe the world, characters, or opening situation...",
        height=150
    )

    temperature = st.slider(
        "Creativity (Temperature)",
        0.0, 1.0, 0.7, step=0.1
    )

    # -----------------------------
    # Start Story Button
    # -----------------------------
    if st.button("✨ Start the Story"):
        if not title.strip():
            st.warning("Please enter a story title.")
            return

        if not initial_hook.strip():
            st.warning("Please provide an initial hook or setting.")
            return

        payload = {
            "title": title,
            "genre": genre,
            "initial_hook": initial_hook,
            "temperature": temperature
        }

        with st.spinner("Generating opening paragraph..."):
            res = requests.post(API_START, json=payload)
            data = res.json()

        # Save story to session state
        st.session_state.story = data["opening_paragraph"]
        st.session_state.title = title
        st.session_state.genre = genre

        st.success("Story started! Go to the Main Story View.")
        st.write("### Opening Paragraph")
        st.write(data["opening_paragraph"])