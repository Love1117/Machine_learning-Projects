import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Movie Recommender",
    layout="wide"
)

st.title("🎬 AI Movie Recommendation System")

movie_name = st.text_input(
    "Enter Movie Name"
)

if st.button("Recommend"):

    response = requests.post(
        f"{API_URL}/recommend",
        json={"title": movie_name}
    )

    data = response.json()

    if "recommendations" in data:

        st.subheader("Recommended Movies")

        cols = st.columns(5)

        for idx, movie in enumerate(data["recommendations"]):

            with cols[idx % 5]:

                st.image(movie["poster"])

                st.write(movie["title"])

    else:
        st.error(data["error"])
