import re

def simplify_response(text):
    text = remove_redundancy(text)
    text = add_formatting(text)
    return text.strip()

def remove_redundancy(text):
    # Example: Remove duplicate lines or repeating explanations
    lines = list(set(text.split("\n")))
    return "\n".join(line.strip() for line in lines if line.strip())

def add_formatting(text):
    # Example: Replace common patterns with markdown
    text = re.sub(r"(Quantum computing.*?)\.", r"🔹 \1.", text)
    text = text.replace("**", "")  # remove unnecessary bold markers
    return text
