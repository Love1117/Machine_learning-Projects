import streamlit as st
from streamlit_searchbox import st_searchbox
import requests
import pandas as pd
import joblib

# Load songs dataset
songs = joblib.load("models/songs.joblib")

# Create song list
song_list = songs["track_name"].drop_duplicates().tolist()

# Streamlit settings
st.set_page_config(
    page_title="Music Recommendation",
    layout="wide"
)

st.title("🎵 Music Recommendation System")

# SEARCHABLE DROPDOWN
selected_song = st_searchbox(

    "Search and Select Song",

    song_list,

    index=None,

    placeholder="Type song name here..."

)

API_URL = "http://fastapi:8000/recommend"

# Button
if st.button("Recommend"):

    if selected_song:

        response = requests.post(

            API_URL,

            json={"track_name": selected_song}

        )

        if response.status_code == 200:

            data = response.json()

            recommendations = data["recommendations"]

            st.subheader("Recommended Songs")

            cols = st.columns(5)

            for index, song in enumerate(recommendations):

                with cols[index % 5]:

                    # POSTER
                    st.image(
                        song["poster"],
                        use_container_width=True
                    )

                    # SONG TITLE
                    st.markdown(
                        f"""
                        <h4 style='margin-bottom:0px;'>
                        {song['music_title']}
                        </h4>
                        """,
                        unsafe_allow_html=True
                    )

                    # ARTIST
                    st.markdown(
                        f"""
                        <p style='color:gray; margin-top:0px;'>
                        {song['artist_name']}
                        </p>
                        """,
                        unsafe_allow_html=True
                    )

        else:
            st.error("Song not found")