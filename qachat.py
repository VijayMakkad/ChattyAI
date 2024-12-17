from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import time  # For simulating stream delay (if needed)

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Function to get Gemini response in chunks
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit App Configuration
st.set_page_config(page_title="Q&A Chatbot")
st.markdown(
    """
    <h1 style='text-align: center; color: #f4f4f4;'>ChattyAI</h1>
    """,
    unsafe_allow_html=True
)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input field for the user's question
question = st.text_input("Ask a question:")

# Submit button
if st.button("Send"):
    if not question.strip():  # Alert if input is empty
        st.warning("Please enter a question before submitting!")
    else:
        with st.spinner("Generating response..."):  # Add a spinner during response generation
            response_placeholder = st.empty()  # Placeholder for streaming output
            full_response = ""
            
            # Stream the response in chunks
            for chunk in get_gemini_response(question):
                if chunk.text:  # Ensure the chunk has valid content
                    full_response += chunk.text
                    response_placeholder.write(full_response)  # Update the placeholder dynamically
                    time.sleep(0.05)  # Simulate streaming delay for better user experience
            
            # Append the question and response to chat history
            st.session_state["chat_history"].append({"question": question, "response": full_response})

# Display chat history
if st.session_state["chat_history"]:
    st.write("### Chat History:")
    for chat in st.session_state["chat_history"]:
        st.write(f"**User:** {chat['question']}")
        st.write(f"**Bot:** {chat['response']}")
