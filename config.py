import os
from dotenv import load_dotenv

load_dotenv()

# API Key for Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

OUTPUT_JSON_PATH = "output/conversations.json"

# Model Configurations
GEMINI_MODEL_NAME = "gemini-1.5-flash-8b"
QUERY_LIMIT = 10

# Streamlit UI Configs
STREAMLIT_TITLE = "PIISA-Customer-Service"
UPLOAD_FILE_TYPES = ["xlsx"]
