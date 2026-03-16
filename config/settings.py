import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

LLM_API_KEY = os.getenv("LLM_API_KEY") # Groq API Key