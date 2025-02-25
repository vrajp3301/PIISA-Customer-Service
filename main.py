import streamlit as st
import json
import google.generativeai as genai
from pipelines.data_loader import load_queries
from pipelines.chat_generator import generate_conversation
from pipelines.storage import save_to_json
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME, OUTPUT_JSON_PATH

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def main():
    st.title("PIISA-Customer-Service")
    
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
    
    if uploaded_file:
        queries = load_queries(uploaded_file)
        model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)  

        if st.button("Generate Conversations"):
            conversations = [generate_conversation(q, model) for q in queries[:5]]
            
            for conv in conversations:
                st.text_area("Generated Conversation", value=conv, height=200)
            
            save_to_json(conversations, OUTPUT_JSON_PATH)
            
            st.download_button(
                label="Download Conversations",
                data=json.dumps(conversations, indent=4),
                file_name="conversations.json",
                mime="application/json"
            )

if __name__ == "__main__":
    main()
