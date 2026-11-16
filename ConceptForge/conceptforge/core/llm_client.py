"""Gemini client for text and structured generation."""

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()

DEFAULT_MODEL = "gemini-3.5-flash-lite"


def get_model_name() -> str:
    return os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL


def _api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "your_api_key_here":
        raise RuntimeError(
            "Missing GEMINI_API_KEY. Put it in your existing .env beside app.py."
        )
    return api_key


def generate_text(prompt: str) -> str:
    client = genai.Client(api_key=_api_key())
    try:
        response = client.models.generate_content(
            model=get_model_name(), contents=prompt
        )
    finally:
        client.close()

    if not response.text or not response.text.strip():
        raise RuntimeError("Gemini returned no Markdown text.")
    return response.text.strip()


def generate_structured(prompt: str, schema: type[BaseModel]) -> BaseModel:
    client = genai.Client(api_key=_api_key())
    try:
        response = client.models.generate_content(
            model=get_model_name(),
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=schema,
            ),
        )
    finally:
        client.close()

    if isinstance(response.parsed, schema):
        return response.parsed
    if response.parsed is not None:
        return schema.model_validate(response.parsed)
    if response.text:
        return schema.model_validate_json(response.text)
    raise RuntimeError("Gemini returned no structured content.")
