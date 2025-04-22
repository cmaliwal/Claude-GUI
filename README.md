# Claude-GUI
About Mini app where Claude moves the mouse to interact with an HTML page, and uses that interaction to trigger or reflect something in a Flask backend.

To install and set up the project locally, follow these steps:

**Note:** Python version **>= 3.11** is required.

1. Create and activate the virtual environment 
 ```bash
   # On macOS/Linux
   python3.11 -m venv .venv
   source .venv/bin/activate

   # On Windows (PowerShell)
   python3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   
2. Install dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. Create your .env file using env.example:
    ```bash
        cp example.env .env
    ```  
Run the App

Open terminal:
    
1. Terminal: Start the mouse interaction script
    ```bash
    python mouse_demo.py
    ```

Claude will:

- Start the Flask app in the background.
- Take screenshots to understand what's on screen.
- Launch (or attempt to launch) Firefox.
-Try to interact with the GUI using the tools.

### Current Status

- Screenshot functionality works.
- Claude can visually recognize the interface and describe UI components.
- Firefox can be launched using the bash tool.
- Mouse clicks via the computer tool are being invoked but do not yet trigger actual interactions.

[Screencast from 04-21-2025 06_46_17 PM.webm](https://github.com/user-attachments/assets/ea08f238-799d-41d0-8ea3-a72b8ea79f39)


### Future Scope of Improvements

Here’s what we plan to improve or implement next:
- Make mouse click actions actually affect the browser (functional GUI interaction)
- Detect and interact with GUI elements based on visual position or text (e.g., click "Yes" button by name)
