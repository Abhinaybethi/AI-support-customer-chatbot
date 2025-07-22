# app.py
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Streamlit UI Setup
st.set_page_config(page_title="AIxSupport Chatbot", page_icon="🧠")
st.title("🤖 AI Support - Smart Customer Chatbot")

# Session state for conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send request to backend (router.py)
    try:
        backend_url = "http://localhost:5000/chat"
        response = requests.post(backend_url, json={"query": user_input})
        ai_response = response.json()["response"]
    except Exception as e:
        ai_response = "⚠️ Error: Could not get response from AI."

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
