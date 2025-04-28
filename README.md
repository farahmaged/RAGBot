## Overview

**RAGBot** is a dockerized application designed to facilitate intuitive question-answering from uploaded documents. It uses the **Retrieval-Augmented Generation (RAG)** technique to retrieve contextually relevant information from documents and process this data through a large language model (LLM) to provide accurate and coherent responses.

## Usage Instructions

1. **Obtain an API Key:**
   You need an API key from either OpenAI or Google. Obtain your key from:
   - [Google](https://ai.google.dev/)
   - [OpenAI](https://platform.openai.com/account/api-keys)

2. **Configure API Keys:**
   Store your API keys in a `.env` file. `.env.example` file is included for guidance.

3. **Set Up Backend and Frontend:**
   Run the following command to start both the backend and frontend:

    ```shell
    docker compose up
    ```

   This command will start all necessary services. Make sure Docker is installed and configured on your machine.

4. **Access the Application:**
   Open your browser and navigate to [http://localhost:8501/](http://localhost:8501/) to access the frontend.

5. **Upload Document:**
   Upload the PDF document you want to inquire about.

6. **Ask Questions:**
   Enter your question in the chat input section and wait for the system to generate a response.

## Key Features

- **RAG-Based Question-Answering:** Efficiently answers user questions by retrieving relevant document context and processing it through an LLM.
- **Seamless Integration:** Both frontend and backend are containerized with Docker for easy deployment and scalability.
- **Interactive UI:** Built using [Streamlit](https://streamlit.io/), offering a simple and user-friendly interface.
- **Efficient Document Retrieval:** Uses [Chroma DB](https://www.trychroma.com/) for vector-based document retrieval, ensuring fast and scalable responses.
- **Customizable API Integration:** Easily configurable API keys for access to powerful language models.
