# gemini api client 
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

DEFAULT_MODEL = "gemini-3.5-flash-lite"

def get_model_name() -> str:
    # read configured model name, fallback to default if not set or empty
    return os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL

def generate_text(prompt: str) -> str:
    # generate text with Gemini, raising clear errors for invalid setup/output
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model=get_model_name(),
            contents=prompt,
        )
    finally:
        client.close()

    result = response.text
    if not result or not result.strip():
        raise RuntimeError("Gemini returned no text.")
    return result.strip()
