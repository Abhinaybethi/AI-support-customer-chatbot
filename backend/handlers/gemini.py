import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Gemini Pro model
model = genai.GenerativeModel('models/gemini')  # ✅ correct path


def format_context_for_prompt(context):
    formatted = ""
    for turn in context:
        formatted += f"User: {turn['user']}\nBot: {turn['bot']}\n"
    return formatted.strip()

def gemini_query(user_id: str, user_msg: str, context: list) -> str:
    # Format conversation history
    formatted_context = format_context_for_prompt(context)
    full_prompt = f"""
You are a helpful and smart customer support AI assistant.

Use the following chat history to understand the context and respond simply:

{formatted_context}

User: {user_msg}
Bot:"""

    try:
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        return f"❗ Error getting Gemini response: {e}"
