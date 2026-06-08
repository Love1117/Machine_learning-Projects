from fastapi import FastAPI, HTTPException
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.services.model_loader import products , vector



def strikethrough_text(text):
    return ''.join([char + '\u0336' for char in str(text)])



def recommend_products(request: ProductRequest):
  try:
    requested_category = request.category

    idx = products[products["category"].str.lower() == requested_category.lower()].index

    if idx.empty:
      raise HTTPException(status_code=404,
      detail=f"Category '{requested_category}' not found")
            
    # Use the first matching phone's vector as the reference for similarity
    # Reshape to (1, -1) because cosine_similarity expects 2D arrays
    category_reference_vector = vector[idx[0]].reshape(1, -1)

    # Calculate cosine similarity between the reference vector and all phone vectors
    sim_scores_raw = cosine_similarity(category_reference_vector, vector).flatten()

    # Pair each similarity score with its original index and sort in descending order
    sim_scores = sorted(list(enumerate(sim_scores_raw)),
                        reverse=True,  key= lambda item: item[1])

    recommendations = []

    # Get top 10 recommendations, skipping the first one (which is the input phone itself)
    for i in sim_scores[1:11]:
      recommended_products = products.iloc[i[0]]
      market_price_formatted = strikethrough_text(recommended_products['market_price'])

      recommendations.append({
                "image_url": recommended_products['image_url'],
                "product_name": recommended_products['product'],
                "sale_price": f"${recommended_products['sale_price']}",
                "market_price": f"${market_price_formatted}"
            })
    
    return {
            "requested_category": requested_category,
            "recommendations": recommendations}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
