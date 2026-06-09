import streamlit as st
import requests

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

st.title("🎬 AI Product Recommendation System")

# GET PRODUCTS FROM FASTAPI
try:
    response = requests.get(
        f"{API_URL}/Products"
    )

    brands = response.json()["Products"]

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
                "brand": selected_brand
            }
        )

        recommendations  = response.json()

        st.subheader(
                f"Top Recommendations for {selected_brand}"
            )

        cols = st.columns(5)

        for idx, phone in enumerate(recommendations):

            with cols[idx % 5]:

                img_url = phone.get("image_url")

                if not img_url or img_url == "N/A" or not is_valid_image(img_url):
                    img_url = DEFAULT_IMAGE

                st.image(
                             img_url,
                             use_container_width=True)

                st.markdown(
                f"""
                <div style="
                border:1px solid #ddd;
                border-radius:12px;
                padding:10px;
                margin-bottom:15px;
                min-height:200px;
                ">
                <h5>{phone['product_name']}</h5>

                <p>{phone['rating']}</p>

                <p>
                    <b>{phone['sale_price']}</b>
                </p>

                <p>
                    {phone['market_price']}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )
