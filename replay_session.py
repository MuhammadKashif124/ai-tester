# record_session.py
import asyncio
from browser_use.llm import ChatGoogle
from browser_use import *
from dotenv import load_dotenv
import json

# Make sure your .env file is correctly formatted
load_dotenv()

async def record_actions():
    """
    Runs the full Agent with an LLM to generate and save a plan of browser actions.
    """
    print("--- Starting Recording Phase (with LLM) ---")
    
    # Initialize the LLM
    llm = ChatGoogle(model='gemini-2.5-flash') # Or your preferred model
    # browser_session = BrowserSession(cdp_url="http://localhost:9242")

    #read initial actions from the json file
    with open("initial_actions.json", "r") as file:
        initial_actions = json.load(file)

    agent = Agent(
        task="Do nothing as I have already replayed the actions using initial actions.",
        initial_actions=initial_actions,
        # browser_session=browser_session,
        llm=llm,
        save_conversation_path="logs/proposal_manualf",
        
    )

    # Run the agent to perform the task
    result = await agent.run()

    print()
    print()
    print("\n--- Recording Phase Complete ---")
    print()
    print()
    print(f"Agent output: {result}")
    print()
    print()
    print("Browser actions have been saved to the 'logs/amazon_search_session' directory.")

if __name__ == "__main__":
    asyncio.run(record_actions())