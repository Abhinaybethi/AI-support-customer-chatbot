# 🧠 AI Support - Advanced AI Customer Support Bot

AIxSupport is an intelligent, voice-enabled, memory-aware chatbot powered by Gemini, Perplexity, and DeepSeek APIs. Designed for real-time reasoning, web access, and simplified answers for customer support.

---

## 🚀 Features

- ✅ Real-time Web Reasoning using Gemini, Perplexity & DeepSeek
- 🧠 Session Memory + Conversation History
- 🗣️ Voice Input + Text-to-Speech Output (Streamlit + JavaScript)
- 📄 Simplified Answer Summarization
- 🌐 Modular API Integration
- ☁️ AWS-ready Architecture

---

## 📁 Project Structure

```bash
AIxSupport/
├── backend/
│   ├── app.py
│   ├── handlers/
│   │   ├── gemini.py
│   │   ├── perplexity.py
│   │   └── deepseek.py
│   ├── aggregator.py
│   ├── router.py
│   ├── simplifier.py
│   ├── memory.py
│   └── config.py
├── frontend/
│   ├── app.py (Streamlit)
│   └── assets/
│       └── voice.js
├── static/
│   └── screenshots/
├── requirements.txt
├── .env
└── README.md
