import requests
import pandas as pd
import json
import time

# Load Bluesky dataset
file_path = "test.csv"
df = pd.read_csv(file_path)

# LM Studio API URL for embeddings
API_URL = "http://127.0.0.1:1234/v1/embeddings"

# Function to get embeddings from LM Studio
def get_embedding(text):
    payload = {
        "model": "text-embedding-mxbai-embed-large-v1",
        "input": text
    }
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        return response.json()["data"][0]["embedding"]  # Extract embedding
    else:
        print(f"❌ Failed to get embedding for text: {text[:50]}... | Error: {response.text}")
        return None

# Apply embedding function to all posts (with delay to avoid overloading LM Studio)
embeddings = []
for i, text in enumerate(df["text"]):
    embeddings.append(get_embedding(text))
    time.sleep(0.1)  # Add a short delay to avoid overwhelming LM Studio

df["embeddings"] = embeddings

# Save the data with embeddings
df.to_csv("embedded_test.csv", index=False)

print("✅ Embeddings generated and saved to embedded_test.csv")
