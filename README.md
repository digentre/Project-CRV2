# Countrunner V2

A Streamlit application that uses AI-powered vector search to find and count records in a business to business database. The app processes natural language queries and searches through documents using OpenAI embeddings and Pinecone vector database.

## Features

- Natural language query processing
- AI-powered semantic search using OpenAI embeddings
- Vector similarity search with Pinecone
- Real-time result counting
- Support for complex queries and questions

## Example Queries

You can ask questions naturally, such as:
- "How many companies in Hampshire?"
- "What records mention London?"
- "Where are the businesses located?"
- "How many financial services companies?"

## Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: OpenAI API (text-embedding-ada-002 model)
- **Vector Database**: Pinecone
- **Language**: Python 3.x

## Requirements

bash
strealit
openai
pinecone-client
python-dotenv

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_key_here
   PINECONE_API_KEY=your_pinecone_key_here
   ```

4. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Environment Variables

The following environment variables are required:
- `OPENAI_API_KEY`: Your OpenAI API key
- `PINECONE_API_KEY`: Your Pinecone API key

## How It Works

1. User enters a natural language query
2. App processes and cleans the query (removes stop words, etc.)
3. OpenAI creates embeddings for the search terms
4. Pinecone searches for similar vectors in the database
5. App counts and displays relevant matches

## Security

- API keys are stored in environment variables
- Keys are never exposed in the code
- `.env` file is included in `.gitignore`

## Deployment

The app is deployed on Streamlit Cloud and can be accessed at [https://countrunnerv2.streamlit.app/].

## Contributing

Feel free to submit issues and enhancement requests!

## License

   MIT License

   Copyright (c) [2024] Emailmovers Limited

   Permission is hereby granted...

## Contact

duncan@emailmovers.com
