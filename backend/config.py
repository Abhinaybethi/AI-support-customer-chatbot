import os
from dotenv import load_dotenv

# Load .env file once
load_dotenv()

def get_env(var_name, default=None):
    """Helper to fetch environment variable safely."""
    return os.getenv(var_name, default)

# API Keys
GEMINI_API_KEY = get_env("GEMINI_API_KEY")
PERPLEXITY_API_KEY = get_env("PERPLEXITY_API_KEY")
DEEPSEEK_API_KEY = get_env("DEEPSEEK_API_KEY")

# App Config
APP_ENV = get_env("APP_ENV", "production")
DEBUG_MODE = get_env("DEBUG", "false").lower() == "true"
