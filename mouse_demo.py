"""
Script that uses Claude's Computer Use capability to interact with a simple Flask app
that has Yes and No buttons.
"""

import os
import asyncio
import subprocess
import time
import signal
import sys
from anthropic import Anthropic
from anthropic.types.beta import BetaMessageParam
from dotenv import load_dotenv
load_dotenv()
# Import the necessary modules from the Anthropic tools
from tools.loop import sampling_loop, APIProvider

# Your Anthropic API key - replace with your actual key or set as environment variable
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# The prompt for Claude
PROMPT = """
Please follow these steps:
check desktop to find firefox,
Open Firefox by clinking its icon and navigate to http://localhost:5000 url,
Take a screenshot to see the page, move the cursor to "Yes" text button
First Click on the "Yes" text button.
Take another screenshot to see what happened, then move the cursor to "No" text button,
Then Click on the "No" button
Take a final screenshot to see the result
Describe what you did and what happened at each step
"""

# Flask process variable
flask_process = None

def start_flask_server():
    """Start the Flask server as a subprocess"""
    global flask_process
    print("Starting Flask server...")
    flask_process = subprocess.Popen(
        [sys.executable, "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Give the server time to start
    time.sleep(2)
    print("Flask server started.")

def stop_flask_server():
    """Stop the Flask server subprocess"""
    global flask_process
    if flask_process:
        print("Stopping Flask server...")
        if sys.platform == "win32":
            flask_process.terminate()
        else:
            os.killpg(os.getpgid(flask_process.pid), signal.SIGTERM)
        flask_process = None
        print("Flask server stopped.")

async def output_callback(content_block):
    """Callback function to handle Claude's output"""
    if content_block["type"] == "text":
        print(f"Claude: {content_block['text']}")
    elif content_block["type"] == "tool_use":
        print(f"Claude is using tool: {content_block['name']}")

async def tool_output_callback(tool_result, tool_use_id):
    """Callback function to handle tool results"""
    if tool_result.output:
        print(f"Tool output: {tool_result.output[:100]}..." if len(tool_result.output) > 100 else f"Tool output: {tool_result.output}")
    if tool_result.error:
        print(f"Tool error: {tool_result.error}")
    if tool_result.base64_image:
        print("Tool returned an image")

def api_response_callback(request, response, exception):
    """Callback function to handle API responses"""
    if exception:
        print(f"API error: {exception}")
    elif response:
        print(f"API response status: {getattr(response, 'status_code', 'N/A')}")
        
async def main():
    """Main function to run the Claude script"""
    if not ANTHROPIC_API_KEY:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.")
        print("Please set your Anthropic API key with:")
        print("export ANTHROPIC_API_KEY=your_api_key_here")
        return

    # Start the Flask server
    start_flask_server()
    
    try:
        # Initialize the messages with the prompt
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": PROMPT
                    }
                ]
            }
        ]
        
        # Run the sampling loop
        await sampling_loop(
            model="claude-3-7-sonnet-20250219",
            provider=APIProvider.ANTHROPIC,
            system_prompt_suffix="",
            messages=messages,
            output_callback=output_callback,
            tool_output_callback=tool_output_callback,
            api_response_callback=api_response_callback,
            api_key=ANTHROPIC_API_KEY,
            max_tokens=4096,
            tool_version="computer_use_20250124",
            thinking_budget=1024,
        )
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Stop the Flask server when done
        stop_flask_server()

if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())