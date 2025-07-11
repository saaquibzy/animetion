import os
from dotenv import load_dotenv

load_dotenv()

# AI/Cloud API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")           # OpenAI (script generation)
HF_TOKEN = os.getenv("HF_TOKEN")                       # Hugging Face (face/image generation)
# COQUI_API_KEY = os.getenv("COQUI_API_KEY")           # Not needed if using HF TTS

# Instagram Graph API credentials
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
IG_USER_ID = os.getenv("IG_USER_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

# Directory paths
VOICES_DIR = "voices"

# Character to speaker type mapping for TTS
CHARACTER_VOICE_MAP = {
    "narrator": "female",  # or "male"
    "male": "male",
    "female": "female"
    # Add more as needed
}