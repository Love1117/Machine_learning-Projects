from fastapi import FastAPI, HTTPException
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.services.model_loader import products , vector



def strikethrough_text(text):
    return ''.join([char + '\u0336' for char in str(text)])



def recommend_products(request: ProductRequest):
  try:
    requested_brand = request.brand

    idx = phone_data[phone_data["brand"].str.lower() == requested_brand.lower()].index

    if idx.empty:
      raise HTTPException(status_code=404,
      detail=f"brands '{requested_brand}' not found")
            
    # Use the first matching phone's vector as the reference for similarity
    # Reshape to (1, -1) because cosine_similarity expects 2D arrays
    brand_reference_vector = vector[idx[0]].reshape(1, -1)

    # Calculate cosine similarity between the reference vector and all phone vectors
    sim_scores_raw = cosine_similarity(brand_reference_vector, vector).flatten()

    # Pair each similarity score with its original index and sort in descending order
    sim_scores = sorted(list(enumerate(sim_scores_raw)),
                        reverse=True,  key= lambda item: item[1])

    recommendations = []

    # Get top 10 recommendations, skipping the first one (which is the input phone itself)
    for i in sim_scores[1:11]:
      recommended_phone = phone_data.iloc[i[0]]
      market_price_formatted = strikethrough_text(recommended_phone['market_price'])

      recommendations.append({
                "image_url": recommended_phone['image_url'],
                "product_name": recommended_phone['name'],
                "rating": f"{recommended_phone['rating']} out of 5 stars ({recommended_phone['ratings_reviews']}) Total comments",
                "sale_price": f"{recommended_phone['discount']} ${recommended_phone['Sale_Price']}",
                "market_price": f"${market_price_formatted}"
            })
    
    return {
            "requested_phone": requested_brand,
            "recommendations": recommendations}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
