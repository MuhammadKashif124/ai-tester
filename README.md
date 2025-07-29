# AI-Tester

An automated browser testing tool powered by AI that records and replays web interactions with perfect reproducibility. Ideal for QA testing, regression testing, and automated web workflows.


## Features

- **AI-Powered Recording**: Uses LLM (Gemini-2.5-Pro) to intelligently navigate websites and create reproducible test scenarios
- **Precise Replay**: Exactly reproduces recorded browser sessions with high reliability
- **Wait-State Management**: Automatically handles page loading and element stability
- **JSON Action Format**: Uses a structured, human-readable format for all browser actions
- **Chrome Integration**: Connects to Chrome via the Chrome DevTools Protocol

## Prerequisites

- Python 3.8+
- Chrome browser
- Chrome user profile directory

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MuhammadKashif124/ai-tester.git
   cd ai-tester
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the browser-use library:
   - Locate the service.py file in the browser_use package (.venv\Lib\site-packages\browser_use\agent\service.py)
   - Search the line: `if orig_target_hash != new_target_hash:`
   - Comment out the `break` statement in this if block (around line 1412)
   - This modification ensures consistent element selection during replay

## Usage

### 1. Start Chrome with remote debugging enabled:

  -  After creating folder C:\chrome-daraz-profile, open cmd in that directory and run this:
    
     ```bash
     start chrome --remote-debugging-port=9242 --user-data-dir="C:\chrome-daraz-profile"
     ```

  -  Login the daraz and dont close the browser.

### 2. Record a session:

   ```bash
   python record_session.py
   ```

  -  This will:
            - Connect to your Chrome instance
            - Execute the predefined task (search for "iPhone 14" on Daraz.pk and proceed to checkout)
            - Save the session logs to the logs directory

### 3. Create initial_actions.json:

  -  Extract the recorded actions into the initial_actions.json file from the generated logs.

### 4. Replay the session:

   ```bash
   python replay_session.py
   ```
  
  -  This will replay the exact same sequence of actions using the initial_actions.json file.

## Example Workflow

  -  The default task demonstrates a complete e-commerce workflow:
    
      1. Navigate to Daraz.pk
      2. Search for "iPhone 14"
      3. Click on the first product
      4. Add to cart
      5. Proceed to checkout
      6. Navigate to payment

## Customization

  -  Modify the `task` variable in record_session.py to create different test scenarios.

## License

  -  This project is licensed under the MIT License - see the LICENSE file for details.