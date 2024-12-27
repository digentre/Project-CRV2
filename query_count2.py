import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from pinecone import Pinecone
import openai

# Initialize OpenAI and Pinecone
openai.api_key = os.getenv("OPENAI_API_KEY")
api_key = os.getenv("PINECONE_API_KEY")
if not api_key or not openai.api_key:
    raise ValueError("Both PINECONE_API_KEY and OPENAI_API_KEY environment variables must be set!")

pc = Pinecone(api_key=api_key)

# Connect to the Pinecone index
index_name = "project-crv2"
index_info = pc.describe_index(index_name)
index = pc.Index(index_info.name)

# Simplified query text
query_text = "Hampshire"

# Generate embedding for the query
def get_embedding_safe(text, model="text-embedding-ada-002"):
    try:
        response = openai.Embedding.create(input=text, model=model)
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"Error generating embedding for query: {text}\n{e}")
        return None

query_embedding = get_embedding_safe(query_text)

# Query the Pinecone index
if query_embedding:
    results = index.query(
        vector=query_embedding,
        top_k=100,  # Retrieve enough results to analyze
        include_metadata=True
    )

    # Count how many records mention "Hampshire"
    count = sum(1 for match in results["matches"] if "hampshire" in match["metadata"].get("Data", "").lower())

    print(f"Count of records mentioning 'Hampshire': {count}")
else:
    print("Failed to generate query embedding.")
