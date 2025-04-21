# Claude-GUI
About Mini app where Claude moves the mouse to interact with an HTML page, and uses that interaction to trigger or reflect something in a Flask backend.

To install and set up the project locally, follow these steps:

NOTE: Will need to use python version >= 3.11 

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
        cp example .env

Run the App

Open two terminals:

1. Terminal: Start the Flask server  
    python app.py
    
2. Terminal: Start the mouse interaction script
    python mouse_demo.py
