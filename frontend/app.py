import base64
import logging
import requests
import streamlit as st

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

st.title("RAGBot - Q&A System Using RAG")

st.sidebar.title("Choose file")
uploaded_file = st.sidebar.file_uploader(
    label="Choose a file", type="pdf", accept_multiple_files=False
)

message = st.chat_message("assistant")
message.write("Ask a question regarding your document")

prompt = st.chat_input("Enter your question here")
if prompt and uploaded_file is not None:
    message = st.chat_message("user")
    logger.info(f"Received user question: {prompt}")
    message.write(prompt)
    message = st.chat_message("assistant")
    message.write("Thinking...")

    logger.info("Converting uploaded PDF to base64-encoded string for transmission")
    encoded_pdf = base64.b64encode(uploaded_file.read()).decode("ascii")
    json_payload = {"question": prompt, "pdf": encoded_pdf}

    logger.info("Initiating POST request to backend")
    response = requests.post("http://backend:8000/ask", json=json_payload, timeout=120)

    logger.info("Displaying response received from backend")
    message.write(response.json())
