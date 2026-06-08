import streamlit as st
import requests
from app.services.model_loader import phone_data 

DEFAULT_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
def is_valid_image(url):
    try:
        response = requests.head(url, timeout=3)
        return response.status_code == 200
    except:
        return False


API_URL = "http://fastapi:8000"

st.set_page_config(
    page_title="Mobile Recommender",
    layout="wide"
)

st.title("🎬 AI Mobile Recommendation System")

# GET MOBILES FROM FASTAPI
try:
    response = requests.get(
        f"{API_URL}/brands"
    )

    brands = response.json()["brands"]

except:
    st.error("FastAPI server is not running.")
    st.stop()

# SEARCHABLE DROPDOWN
selected_brand = st.selectbox(
    "Search or Select a Phone Brand",
    brands,
    index=None,
    placeholder="Type to search brand..."
)

# RECOMMEND BUTTON
if st.button("Recommend Phones"):

    if not selected_brand:
        st.warning("Please select a brand.")
        st.stop()

    with st.spinner("Finding recommendations..."):

        response = requests.post(
            f"{API_URL}/recommend",
            json={
                "title": selected_brands
            }
        )

        recommendations  = response.json()

        st.subheader(
                f"Top Recommendations for {selected_brands}"
            )

        cols = st.columns(5)

        for idx, phone in enumerate("recommendations"):

            with cols[idx % 5]:

                img_url = phone.get("image_url")

                if not img_url or img_url == "N/A" or not is_valid_image(img_url):
                    img_url = DEFAULT_IMAGE

                    st.image(
                             img_url,
                             use_container_width=True)

                    st.write(phone_data["brand"])
