import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_FALLBAC_API_KEY = os.getenv("GROQ_FALLBAC_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_COLLECTION = "IndustryGradRag"

    gemini_api_key = os.getenv("GEMINI_API_KEY")



settings = Settings()



