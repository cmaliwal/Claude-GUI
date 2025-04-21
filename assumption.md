# Technical Assumptions

Python 3.11 or higher is installed and available in the system path.
anthropic, dotenv, and other required packages are installed via pip install -r requirements.txt.
firefox browser is installed and accessible via the system path.

The Flask app (app.py) serves an index.html file and listens on http://localhost:5000.

## Environment Assumptions

The system allows for GUI automation (e.g., cursor movement, clicking).

Claude has access to a virtual desktop display and can visually locate UI elements on the screen.

The browser (Firefox) can be launched by desktop icon or CLI, and is the default system browser.

The Anthropic computer_use tool environment is pre-configured and properly running (e.g., inside Docker or VNC with GUI support).

## Runtime Flow Assumptions
Running mouse_demo.py automatically starts the Flask server by launching app.py in the background.

Once launched, the browser should automatically open and navigate to http://localhost:5000.

mouse_demo.py assumes that Claude will be able to identify, move to, and click the "Yes" and "No" buttons on the rendered web page.

The script assumes there is no pop-up or full-screen interference (e.g., alerts, modals) that hides the buttons.

## API and Security Assumptions
A valid ANTHROPIC_API_KEY is set in the environment (.env file or system environment).

Network access is available for the script to communicate with Anthropic's API servers.

## Known Limitations
Currently, the browser only opens but no mouse movement or clicking occurs. This is a known limitation, and troubleshooting is ongoing.

No GUI automation is currently being executed—Claude cannot yet simulate mouse actions or detect the HTML structure programmatically.

Script assumes a single-user and single-session flow — parallel execution may cause unexpected behavior.

## Impact on Implementation

These assumptions directly impact several aspects of the project:

1. **Browser Compatibility**: The project is specifically designed for Firefox and may not work with other browsers without modification.
   
2. **Environment Requirements**: The code requires specific environment setup with GUI capabilities that may not be available in all deployment scenarios.
   
3. **API Dependencies**: The project relies on Anthropic's computer_use tool which is still evolving and may change in future API versions.
   
4. **Current Limitations**: As noted in the Known Limitations section, full mouse automation functionality is not yet working as intended.
