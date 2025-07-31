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
    llm = ChatGoogle(model='gemini-2.5-flash') # Or your preferred model
    browser_session = BrowserSession(cdp_url="http://localhost:9242")

#     task = f"""
# Your task is to create a perfectly repeatable log of actions. The most critical instruction is to **wait for the page to fully and completely load before every single action.** This pause is essential for ensuring element indices are stable.

# Follow these steps precisely, pausing before each one:

# 1.  **Go** to `https://www.daraz.pk/`.
# 2.  **Wait and Verify:** Pause for a few seconds until the page is completely stable and no new elements are appearing.
# 3.  **Type:** Locate the main search bar and enter the text 'iPhone 14'.
# 4.  **Click:** Press the search button.
# 5.  **Wait and Verify:** Wait until the search results page is fully loaded and no new elements are shifting or rendering.
# 6.  **Click:** Click on the very first product result shown.
# 7.  **Wait and Verify:** Let the product detail page load fully and ensure the page is stable.
# 8.  **Click:** Click the button to add the item to your cart.
# 9.  **Wait and Verify:** Pause until the cart confirmation or popup has completely rendered.
# 10. **Click:** Close the confirmation popup and Open the cart page by clicking the cart icon in the navigation bar (besides the search icon).
# 11. **Wait and Verify:** Wait until the cart page is fully stable.
# 12. **Click:** Select the checkbox or toggle for the added item if required.
# 13. **Click:** Click on the 'Proceed to Checkout' button.
# 14. **Wait and Verify:** Wait until the checkout page is fully stable.
# 15. **Click:** Click on the 'Proceed to Pay' button.

# By carefully waiting before each step, you will generate a reliable action log that will not fail on replay.
# """

    task = f"""
Your task is to perform the given actions. The most critical instruction is to **wait for the page to fully and completely load before every single action.** This pause is essential for ensuring element indices are stable.

Follow these steps precisely, pausing before each one:

1.  **Go** to `https://elekipo.com/admin/authentication`.
2.  **Wait and Verify:** Let the page fully load and stabilize.
3.  **Type:** Enter `user.automation@gmail.com` into the email field.
4.  **Type:** Enter `2Sg$HwH3d0ag` into the password field.
5.  **Click:** Click the login button.
6.  **Wait and Verify:** Wait until the dashboard is fully loaded and navigation is stable.
7.  **Hover & Click:** Hover over the 4th item on the left navigation bar (shows "Commerce" on hover), then click it.
8.  **Wait and Verify:** Let the page load completely and wait for the blue `+ New Proposal` button.
9.  **Click:** Click the `+ New Proposal` button.
10. **Wait and Verify:** Pause until the proposal form is fully loaded and all fields are rendered.

Now fill the form:

11. **Type:** Subject = `Testing browser use 2`.
12. **Click:** Click on the Contact/Client dropdown. Wait for it to appear.
13. **Type & Select:** Search and select `avialdo_u6oum6`.
14. **Select:** Status = `Open`.
15. **Type:** To = `test@gmail.com`.
16. **Type:** Address = `xyz`.
17. **Type:** City = `zz`.
18. **Type:** State = `zz`.
19. **Click:** Click on the Country dropdown.
20. **Type & Select:** Search and select `United States`.
21. **Type:** Zip Code = `12345`.
22. **Type:** Email = `xyz@gmail.com`.
23. **Type:** Phone = `+923061111111`.

Now in the Add Item section:

24. **Click:** Click on the "Add Item" box.
25. **Wait and Verify:** Wait for the dropdown to appear.
26. **Select:** Choose the 1st item from the list.
27. **Select:** Set Tax = `GST`.
28. **Click:** Press the blue add (+) button.
29. **Wait and Verify:** Wait for the item to be added to the proposal list.
31. **Verify and Click:** After adding the item, click the blue `Save` button at the bottom right of the page.
32. **Wait and Verify:** Wait for the confirmation popup to appear near the URL bar.
33. **Click:** Click the `Leave` button on the popup.

End of task. Remember: every **Wait and Verify** step must ensure the page is **completely stable** before proceeding.
"""

    agent = Agent(
        task=task,
        # browser_session=browser_session,
        llm=llm,
        save_conversation_path="logs/proposal_autof2",
        
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