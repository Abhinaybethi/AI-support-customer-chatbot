import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL_ID = "google/flan-t5-small"
HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"


def ask_huggingface(query: str) -> str:
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": query
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        output = response.json()
        return output[0]["generated_text"] if isinstance(output, list) else str(output)
    except Exception as e:
        return f"[HF API Exception]: {e}"
