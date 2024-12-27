import os
from pinecone import Pinecone, ServerlessSpec

# Set API key and environment
api_key = os.getenv("PINECONE_API_KEY")  # Replace with your API key directly if not using environment variables
if not api_key:
    raise ValueError("PINECONE_API_KEY environment variable is not set!")

pc = Pinecone(api_key=api_key)

# Define index name
index_name = "project-crv2"

# Check if index exists; if not, create it
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,  # Dimension of embeddings from text-embedding-ada-002
        metric="cosine",  # Metric for similarity search
        spec=ServerlessSpec(
            cloud="aws",  # Your cloud provider
            region="us-east-1"  # Your region
        )
    )

# Retrieve the index (use `pc.describe_index()` and `pc.Index` for connection)
index_info = pc.describe_index(index_name)
index = pc.Index(index_info.name)

print(f"Successfully connected to Pinecone index: {index_name}")
