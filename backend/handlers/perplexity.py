import requests
import os
from dotenv import load_dotenv

load_dotenv()

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def ask_perplexity(query: str):
    try:
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
  "model": "pplx-7b-chat",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is blockchain?"}
  ],
  "stream": false
}

        

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()
        answer = reply['choices'][0]['message']['content']
        return answer

    except Exception as e:
        return f"[Perplexity Error]: {str(e)}"
