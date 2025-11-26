import os
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel
from tools import read_user_profile, update_user_profile # Assuming tools.py is in the same directory

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Initialize AsyncOpenAI with Gemini's base URL
gemini_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GEMINI_API_KEY,
)

# Initialize OpenAIChatCompletionsModel for Gemini
gemini_chat_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client,
)

# Define the Agent
chatbot_agent = Agent(
    name="Personal Chatbot with Memory",
    instructions="Greet users by name if known. Detect when users share personal info and save it using tools.",
    tools=[read_user_profile, update_user_profile],
    model=gemini_chat_model,
)
