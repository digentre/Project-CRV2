import os  # Ensure this is included
import pandas as pd
from pinecone import Pinecone, Vector

# Load the data with embeddings
file_path = r"C:\Users\admin\Desktop\Project CRV2\grouped_data_with_embeddings.csv"
data = pd.read_csv(file_path)

# Initialize Pinecone
api_key = os.getenv("PINECONE_API_KEY")  # Ensure your API key is set as an environment variable
if not api_key:
    raise ValueError("PINECONE_API_KEY environment variable is not set!")

pc = Pinecone(api_key=api_key)

# Define index name
index_name = "project-crv2"
index_info = pc.describe_index(index_name)
index = pc.Index(index_info.name)

# Prepare Embeddings for Upload
batch_size = 100
records = []

for idx, row in data.iterrows():
    # Convert embeddings from string to list
    location_embedding = eval(row["Location Embedding"])
    contact_embedding = eval(row["Contact Embedding"])
    company_size_embedding = eval(row["Company Size Embedding"])
    company_type_embedding = eval(row["Company Type Embedding"])

    # Add a record for each group
    records.append(Vector(
        id=f"{row['REFNUM']}_Location",
        values=location_embedding,
        metadata={"Group": "Location", "Data": row["Location"]}
    ))
    records.append(Vector(
        id=f"{row['REFNUM']}_Contact",
        values=contact_embedding,
        metadata={"Group": "Contact", "Data": row["Contact"]}
    ))
    records.append(Vector(
        id=f"{row['REFNUM']}_CompanySize",
        values=company_size_embedding,
        metadata={"Group": "Company Size", "Data": row["Company Size"]}
    ))
    records.append(Vector(
        id=f"{row['REFNUM']}_CompanyType",
        values=company_type_embedding,
        metadata={"Group": "Company Type", "Data": row["Company Type"]}
    ))

    # Upload in batches
    if len(records) >= batch_size:
        index.upsert(vectors=records)
        records = []

# Upload any remaining records
if records:
    index.upsert(vectors=records)

print("Embeddings successfully uploaded to Pinecone!")
