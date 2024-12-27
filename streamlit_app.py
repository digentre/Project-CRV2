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

def extract_search_terms(query):
    # Remove question marks and common question words
    query = query.lower()
    query = query.replace('?', '')
    stop_words = {'how', 'many', 'what', 'where', 'when', 'who', 'why', 'in', 'is', 'are', 'the'}
    words = query.split()
    search_terms = [word for word in words if word not in stop_words]
    return ' '.join(search_terms)

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
        with st.spinner('Searching...'):
            # Extract key search terms
            search_terms = extract_search_terms(query_text)
            st.write(f"Searching for: {search_terms}")  # Debug line
            query_embedding = get_embedding_safe(search_terms)
            
            if query_embedding:
                results = index.query(
                    vector=query_embedding,
                    top_k=100,
                    include_metadata=True
                )
                # Search for each term individually
                search_words = search_terms.split()
                total_count = 0
                for word in search_words:
                    if word:  # Skip empty strings
                        count = sum(1 for match in results["matches"] 
                                  if word.lower() in match["metadata"].get("Data", "").lower())
                        if count > 0:
                            st.write(f"Found {count} records mentioning '{word}'")
                            total_count += count
                
                if total_count > 0:
                    st.success(f"Total relevant records found: {total_count}")
                else:
                    st.warning("No matching records found")
    else:
        st.warning("Please enter a search query") 