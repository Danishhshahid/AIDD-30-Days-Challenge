import chainlit as cl
from agent import chatbot_agent
from agents import Runner

@cl.on_chat_start
async def start():
    """
    This function is called when a new chat session is started.
    It initializes the chatbot agent and sends a welcome message.
    """
    # The chatbot_agent is already initialized in agent.py
    # We can store it in the user_session for later use if needed,
    # but for this simple case, we can directly use the imported agent.
    
    await cl.Message(content="Hello, how can I assist you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """
    This function is called every time a user sends a message.
    It passes the user's message to the chatbot agent and sends the agent's response back to the user.
    """
    # Run the agent with the user's message
    result = await Runner.run(chatbot_agent, message.content)

    # Print/Display tool outputs for debugging
    # The 'result' object might contain details about tool calls and their outputs.
    # For now, we'll just print the final output.
    print(f"Agent final output: {result.final_output}")
    if result.new_items:
        for item in result.new_items:
            if hasattr(item, 'tool_name') and hasattr(item, 'output'):
                print(f"Tool {item.tool_name} output: {item.output}")

    # Send the final response to the UI
    await cl.Message(content=result.final_output).send()