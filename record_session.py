# record_session.py
import asyncio
from browser_use.llm import ChatGoogle
from browser_use import *
from dotenv import load_dotenv

# Make sure your .env file is correctly formatted
load_dotenv()

async def record_actions():
    """
    Runs the full Agent with an LLM to generate and save a plan of browser actions.
    """
    print("--- Starting Recording Phase (with LLM) ---")
    
    # Initialize the LLM
    llm = ChatGoogle(model='gemini-2.5-pro') # Or your preferred model
    # C:\chrome-daraz-profile>start chrome --remote-debugging-port=9242 --user-data-dir="C:\chrome-daraz-profile"
    browser_session = BrowserSession(cdp_url="http://localhost:9242")

    task = f"""
Your task is to create a perfectly repeatable log of actions. The most critical instruction is to **wait for the page to fully and completely load before every single action.** This pause is essential for ensuring element indices are stable.

Follow these steps precisely, pausing before each one:

1.  **Go** to `https://www.daraz.pk/`.
2.  **Wait and Verify:** Pause for a few seconds until the page is completely stable and no new elements are appearing.
3.  **Type:** Locate the main search bar and enter the text 'iPhone 14'.
4.  **Click:** Press the search button.
5.  **Wait and Verify:** Wait until the search results page is fully loaded and no new elements are shifting or rendering.
6.  **Click:** Click on the very first product result shown.
7.  **Wait and Verify:** Let the product detail page load fully and ensure the page is stable.
8.  **Click:** Click the button to add the item to your cart.
9.  **Wait and Verify:** Pause until the cart confirmation or popup has completely rendered.
10. **Click:** Close the confirmation popup and Open the cart page by clicking the cart icon in the navigation bar (besides the search icon).
11. **Wait and Verify:** Wait until the cart page is fully stable.
12. **Click:** Select the checkbox or toggle for the added item if required.
13. **Click:** Click on the 'Proceed to Checkout' button.
14. **Wait and Verify:** Wait until the checkout page is fully stable.
15. **Click:** Click on the 'Proceed to Pay' button.

By carefully waiting before each step, you will generate a reliable action log that will not fail on replay.
"""

    agent = Agent(
        task=task,
        browser_session=browser_session,
        llm=llm,
        save_conversation_path="logs/darazfinal",
        
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