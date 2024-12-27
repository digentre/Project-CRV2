import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

# Load environment variables
load_dotenv()

# Initialize OpenAI and Pinecone
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
api_key = os.getenv("PINECONE_API_KEY")

def get_embedding_safe(text, model="text-embedding-ada-002"):
    try:
        response = client.embeddings.create(
            input=text,
            model=model
        )
        return response.data[0].embedding
    except Exception as e:
        st.error(f"Error generating embedding: {e}")
        return None

# Initialize Pinecone
pc = Pinecone(api_key=api_key)
index = pc.Index("project-crv2")

# Streamlit interface
st.title("Hampshire Record Search")
query_text = st.text_input("Enter your search query:")

if st.button("Search"):
    if query_text:
        with st.spinner('Searching...'):  # Add loading indicator
            query_embedding = get_embedding_safe(query_text)
            if query_embedding:
                results = index.query(
                    vector=query_embedding,
                    top_k=100,
                    include_metadata=True
                )
                # Updated to use the actual query term
                count = sum(1 for match in results["matches"] 
                          if query_text.lower() in match["metadata"].get("Data", "").lower())
                st.success(f"Count of records mentioning '{query_text}': {count}")
    else:
        st.warning("Please enter a search query") 