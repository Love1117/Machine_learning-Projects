import streamlit as st
from streamlit_searchbox import st_searchbox
import requests
import pandas as pd
import joblib
from app.services.model_loader import songs


# Load songs
songs = joblib.load("models/songs.joblib")

# Remove null values
song_list = sorted(
    songs["track_name"].dropna().unique().tolist()
)

# Streamlit page
st.set_page_config(
    page_title="Music Recommendation System",
    layout="wide"
)

st.title("🎵 Music Recommendation System")

# Searchable dropdown
selected_song = st.selectbox(

    "Search Song",

    options=song_list,

    index=None,

    placeholder="Type or select a song"

)

API_URL = "http://fastapi:8000/recommend"

# Recommendation button
if st.button("Recommend"):

    if not selected_song:
        st.warning("Please select a song")

    else:

        with st.spinner("Getting recommendations..."):

            response = requests.post(

                API_URL,

                json={
                    "track_name": selected_song
                }

            )

        if response.status_code == 200:

            data = response.json()

            recommendations = data["recommendations"]

            st.subheader("Recommended Songs")

            cols = st.columns(5)

            for index, song in enumerate(recommendations):

                with cols[index % 5]:

                    # Poster
                    st.image(
                        song["poster"],
                        use_container_width=True
                    )

                    # Music title
                    st.markdown(
                        f"""
                        <h4 style='margin-bottom:0px;'>
                        {song['music_title']}
                        </h4>
                        """,
                        unsafe_allow_html=True
                    )

                    # Artist name
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
