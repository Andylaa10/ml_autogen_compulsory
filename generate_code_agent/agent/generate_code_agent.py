from autogen import ConversableAgent
from config import LLM_CONFIG

# Define prompt for the agent
system_prompt = """
You are now an AI agent capable of writing PYTHON code. 
When you are done writing python function/s and example of how to use the function/s, 
THEN REPLY TERMINATE THE PROCESS AND PRINT TERMINATE IN THE CONSOLE!
"""

# Create the agent responsible for generating code
def create_generate_code_agent() -> ConversableAgent:
    agent = ConversableAgent(
        name="code_agent",
        llm_config=LLM_CONFIG,
        system_message=system_prompt
    )
    return agent

# Create a user proxy for interacting with the agent
def create_user_proxy() -> ConversableAgent:
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    return user_proxy
