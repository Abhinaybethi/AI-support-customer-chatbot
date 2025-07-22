import os
import json
from typing import List, Dict

# Directory to store memory files
MEMORY_DIR = "chat_memory"
os.makedirs(MEMORY_DIR, exist_ok=True)

def get_memory_file(user_id: str) -> str:
    return os.path.join(MEMORY_DIR, f"{user_id}.json")

def load_user_memory(user_id: str) -> List[Dict[str, str]]:
    path = get_memory_file(user_id)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    else:
        return []

def save_user_memory(user_id: str, memory: List[Dict[str, str]]) -> None:
    path = get_memory_file(user_id)
    with open(path, 'w') as f:
        json.dump(memory, f, indent=2)

def update_user_memory(user_id: str, user_msg: str, bot_reply: str) -> None:
    memory = load_user_memory(user_id)
    memory.append({
        "user": user_msg,
        "bot": bot_reply
    })
    save_user_memory(user_id, memory)

def get_recent_context(user_id: str, limit: int = 5) -> List[Dict[str, str]]:
    memory = load_user_memory(user_id)
    return memory[-limit:] if len(memory) > limit else memory
