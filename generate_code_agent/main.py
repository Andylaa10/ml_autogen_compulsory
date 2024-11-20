from agent.generate_code_agent import create_generate_code_agent, create_user_proxy
import argparse

def main():
    # Parse the prompt argument
    parser = argparse.ArgumentParser(
        description="Write a prompt to see the magic happen"
    )
    parser.add_argument("prompt", help="Prompt used to generate some Python code")
    args = parser.parse_args()

    prompt = args.prompt

    # Create user proxy and agent
    user_proxy = create_user_proxy()
    generate_code_agent = create_generate_code_agent()

    # Initiate the chat between the user proxy and the agent
    user_proxy.initiate_chat(
        generate_code_agent,
        message=prompt
    )

if __name__ == '__main__':
    main()
