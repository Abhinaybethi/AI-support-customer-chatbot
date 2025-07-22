from backend.handlers.huggingface import ask_huggingface
from backend.simplifier import simplify_response

# Get response from HuggingFace only
def get_all_responses(query: str) -> dict:
    try:
        hf_response = ask_huggingface(query)
    except Exception as e:
        hf_response = f"[HuggingFace Error]: {str(e)}"
    
    return {
        "HuggingFace": hf_response
    }

# Format the response nicely
def generate_final_answer(results_dict: dict, user_question: str) -> str:
    answer = f"🧠 **Smart Summary for:** _{user_question}_\n\n"
    for source, content in results_dict.items():
        simplified = simplify_response(content)
        answer += f"### 🔹 {source} says:\n{simplified}\n\n"
    return answer.strip()

# Main entrypoint for /chat route
def combine(query: str) -> str:
    results = get_all_responses(query)
    return generate_final_answer(results, query)
