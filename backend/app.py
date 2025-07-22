from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.handlers.hf_api import ask_huggingface

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_msg = data.get("query", "")
    if not user_msg:
        return {"response": "❗ Please provide a valid query."}
    
    reply = ask_huggingface(user_msg)
    return {"response": reply}
