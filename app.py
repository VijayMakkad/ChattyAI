from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import time  # For simulating streaming chunks

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Loading the model
model = genai.GenerativeModel("gemini-1.5-pro")

# Function to get Gemini response in chunks
def get_gemini_response_stream(input, image=None):
    if input != "":
        if image:  # If an image is provided
            response = model.generate_content([input, image], stream=True)
        else:  # If no image is provided
            response = model.generate_content(input, stream=True)
    else:
        yield "Give the prompt!"
        return

    # Simulate response chunks
    for chunk in response:
        yield chunk.text
    return

# Streamlit App
st.set_page_config(page_title="Q&A Demo")
st.markdown(
    """
    <h1 style='text-align: center; color: #f4f4f4;'>ChattyAI</h1>
    """,
    unsafe_allow_html=True
)

# Input and file upload
input = st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.')

# Submit button
submit = st.button("Ask the question")

# Handle the submission
if submit:
    with st.spinner("Getting back to you..."):
        response_placeholder = st.empty()  # Placeholder for dynamic updates
        full_response = ""

        # Get and display response chunks
        for chunk in get_gemini_response_stream(input, image):
            full_response += chunk
            response_placeholder.write(full_response)  # Update placeholder dynamically
            time.sleep(0.05)  # Simulate a delay to visualize chunks

        st.success("Response generated successfully!")
