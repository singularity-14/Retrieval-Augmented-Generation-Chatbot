import streamlit as st
from backend import *

st.title("RAG Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for PDF upload
uploaded_pdfs = st.sidebar.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
button = st.sidebar.button("Submit")

# Check the number of uploaded PDFs
if uploaded_pdfs and button:
    if len(uploaded_pdfs) > 3:
        st.sidebar.error("You can only upload a maximum of 3 PDF files.")
        uploaded_pdfs = []  
    else:
        pdf_text = pdf_processing(uploaded_pdfs)
        text_chunking_uploading(pdf_text) 
        st.sidebar.write(f"Processed {len(uploaded_pdfs)} PDF(s) successfully.")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        # Response from the Gemini 
        response = chain(prompt)

        st.markdown(response)
        
    # Add the Response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
