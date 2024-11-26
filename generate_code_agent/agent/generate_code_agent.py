from autogen import ConversableAgent
from config import LLM_CONFIG

# Define prompt for the agent
system_prompt = """
You are now an AI agent capable of writing PYTHON code. 
When you are done writing python function/s and example of how to use the function/s, 
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
        max_consecutive_auto_reply=2,
        llm_config=LLM_CONFIG,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        code_execution_config={"work_dir": "web", "use_docker": True},
        human_input_mode="NEVER",
        system_message="REPLY TERMINATE THE PROCESS AND PRINT TERMINATE IN THE CONSOLE! IF THE TASK HAS BEEN SOLVED AT FULL SATISFACTION."
    )
    return user_proxy
