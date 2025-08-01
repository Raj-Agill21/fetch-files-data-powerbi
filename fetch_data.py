import requests
import json
import os
import pandas as pd

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET" 
PROJECT_ID = "YOUR_PROJECT_ID"
BASE_URL = "https://developer.api.autodesk.com"
TOKEN_URL = "https://developer.api.autodesk.com/authentication/v2/token"
TOKEN_PATH = "/lakehouse/default/Files/auth/token_store.json"

def refresh_access_token(refresh_token):
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(TOKEN_URL, data=data)
    response.raise_for_status()
    return response.json()

with open(TOKEN_PATH, "r", encoding="utf-8") as f:
    tokens = json.load(f)

new_tokens = refresh_access_token(tokens['refresh_token'])

with open(TOKEN_PATH, "w", encoding="utf-8") as f:
    json.dump(new_tokens, f)

access_token = new_tokens["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}


def get_reviews(headers):
    url = f"{BASE_URL}/construction/reviews/v1/projects/{PROJECT_ID}/reviews"
    return requests.get(url, headers=headers).json().get('results', [])

def get_review_versions(headers, review_id):
    url = f"{BASE_URL}/construction/reviews/v1/projects/{PROJECT_ID}/reviews/{review_id}/versions"
    return requests.get(url, headers=headers).json().get('results', [])

def build_review_with_files(headers):
    all_data = []
    for review in get_reviews(headers):
        for file in get_review_versions(headers, review['id']):
            all_data.append({
                'review_id': review['id'],
                'review_name': review.get('name'),
                'status': review.get('status'),
                'created_at': review.get('createdAt'),
                'file_name': file.get('name'),
                'version_urn': file.get('urn') or file.get('copiedFileVersionUrn'),
                'item_urn': file.get('itemUrn')
            })
    return pd.DataFrame(all_data)

df = build_review_with_files(headers)

spark_df = spark.createDataFrame(df)
spark_df.write.mode("overwrite").saveAsTable("acc_reviews_daily")
