import openai
import pandas as pd
import os

# Use environment variable for API key (set OPENAI_API_KEY beforehand)
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding_safe(text, model="text-embedding-ada-002"):
    try:
        response = openai.Embedding.create(input=text, model=model)
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"Error generating embedding for text: {text}\n{e}")
        return None

# Load the prepared grouped data
grouped_data = pd.read_csv(r"C:\Users\admin\Desktop\Project CRV2\Output-Project CRV2_Single_ANON.csv")

# Prepare Grouped Fields
# 1. Location
grouped_data["Location"] = (
    grouped_data["town"].fillna("") + "; " +
    grouped_data["County"].fillna("") + "; " +
    grouped_data["Postcode"].fillna("") + "; " +
    grouped_data["Region"].fillna("")
).str.strip("; ")

# 2. Contact
grouped_data["Contact"] = (
    grouped_data["job_function"].fillna("") + "; " +
    grouped_data["Job_role_desc"].fillna("") + "; " +
    grouped_data["Job_level_desc"].fillna("")
).str.strip("; ")

# 3. Company Size
grouped_data["Company Size"] = (
    grouped_data["Employee_desc"].fillna("") + "; " +
    grouped_data["Turnover_desc"].fillna("")
).str.strip("; ")

# 4. Company Type
grouped_data["Company Type"] = (
    grouped_data["SIC_desc"].fillna("") + "; " +
    grouped_data["sic_division_desc"].fillna("") + "; " +
    grouped_data["sic_section_desc"].fillna("") + "; " +
    grouped_data["business_class_desc"].fillna("")
).str.strip("; ")

# Generate Embeddings for Each Group
grouped_data["Location Embedding"] = grouped_data["Location"].apply(lambda x: get_embedding_safe(x) if x else None)
grouped_data["Contact Embedding"] = grouped_data["Contact"].apply(lambda x: get_embedding_safe(x) if x else None)
grouped_data["Company Size Embedding"] = grouped_data["Company Size"].apply(lambda x: get_embedding_safe(x) if x else None)
grouped_data["Company Type Embedding"] = grouped_data["Company Type"].apply(lambda x: get_embedding_safe(x) if x else None)

# Save the results with embeddings
grouped_data.to_csv("grouped_data_with_embeddings.csv", index=False)

print("Embeddings generated and saved successfully!")
