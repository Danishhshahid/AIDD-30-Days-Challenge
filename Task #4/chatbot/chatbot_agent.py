import os
from openai import OpenAI
from agents import Agent, OpenAIChatCompletionsModel
from tools import read_user_profile, update_user_profile
from dotenv import load_dotenv

load_dotenv()

def create_chatbot_agent():
    # Initialize the Gemini client using the Base URL
    # The OpenAIChatCompletionsModel will handle the actual API calls
    # using the provided base_url and api_key
    openai_client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    gemini_model = OpenAIChatCompletionsModel(
        openai_client=openai_client,
        model="gemini-2.0-flash",
    )

    # Configure the Agent
    agent = Agent(
        name="PersonalChatbot",
        instructions="Greet users by name if known. Detect when users share personal info and save it using tools.",
        tools=[read_user_profile, update_user_profile],
    )
    return agent, gemini_model
