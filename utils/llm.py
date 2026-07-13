"""
=========================================================
Project : StartupPilotAI
File    : utils/llm.py

Purpose:
---------
This file creates and returns our AI model (LLM).

Every AI agent in our project will use this same
connection instead of creating a new one each time.
=========================================================
"""

# Load environment variables from the .env file
from dotenv import load_dotenv

# Allows us to access environment variables
import os

# LangChain wrapper for Groq models
from langchain_groq import ChatGroq

# Import settings from config.py
from config import MODEL_NAME, TEMPERATURE


# ---------------------------------------------------------
# Load the .env file
# ---------------------------------------------------------
load_dotenv()


# ---------------------------------------------------------
# Read the API key from the environment
# ---------------------------------------------------------
groq_api_key = os.getenv("GROQ_API_KEY")


# ---------------------------------------------------------
# Create the LLM
# ---------------------------------------------------------
llm = ChatGroq(
    api_key=groq_api_key,
    model=MODEL_NAME,
    temperature=TEMPERATURE
)