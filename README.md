# **ChattyAI**

### 🧠 A Gemini-powered Streamlit Chatbot App

**ChattyAI** is a Streamlit-based chatbot application powered by Google's **Gemini LLM API**. It supports text-based interactions, optional image input, and real-time streaming of responses in chunks to provide a smooth user experience.

---

## **Features**

✅ **Real-Time Streaming**:  
- Responses are displayed incrementally, chunk by chunk, for a seamless chat experience.  

✅ **Image Input**:  
- Upload an image along with your question for multimodal responses.  

✅ **Persistent Chat History**:  
- View your previous questions and responses in the same session.  

✅ **User-Friendly Interface**:  
- A clean and intuitive UI built with Streamlit, complete with loading spinners and empty-input alerts.

---

## **Demo**

🎉 Try ChattyAI live here:  
🚀 [ChattyAI Hosted App](https://chattyai-a35j9lzr7tecrqg9tcu.streamlit.app/)

---

## **How to Run the App Locally**

Follow these steps to run ChattyAI on your local machine:

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/ChattyAI.git
cd ChattyAI
```

### **2. Set Up Environment**

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

### **3. Run the App**
```bash
streamlit run app.py
```

This will launch the app in your default web browser at `http://localhost:8501`.

---

## **Dependencies**

The app uses the following libraries:
- **Streamlit**: For the interactive user interface.
- **Pillow**: For image handling.
- **python-dotenv**: For managing environment variables.
- **Google Generative AI**: For integrating the Gemini LLM API.

You can find the complete list of dependencies in `requirements.txt`.

---

## **How It Works**

1. **Input**:  
   - Enter a text-based question.  
   - Optionally, upload an image to provide additional context.

2. **Processing**:  
   - The app sends your input to Google's Gemini API.  
   - Responses are streamed back and displayed incrementally.

3. **Output**:  
   - The response is displayed in real-time, and the conversation is stored in the chat history.

---

## **Folder Structure**

```
ChattyAI/
│
├── app.py                 # Main application file
├── requirements.txt       # Required Python dependencies
├── .env                   # Environment variables (API Key)
└── README.md              # Project documentation
```

---

## **Contributing**

Contributions are welcome! If you'd like to enhance ChattyAI:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## **License**

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute this project as needed.

---

## **Contact**

For questions, feedback, or collaboration, feel free to reach out:  
📧 **vijaymakkad0104@gmail.com**  
🔗 **[LinkedIn: Vijay Makkad](https://www.linkedin.com/in/vijay-makkad-1573681b3/)**  

---

Enjoy chatting with **ChattyAI**! 😊 🚀
