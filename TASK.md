
# Claude-Powered GUI Interaction

## 🧠 Goal
Build a mini app where Claude interacts with a simple HTML page by simulating mouse movements to click buttons. These interactions should trigger or reflect changes in a Flask backend.

---

## 🛠️ What to Build

- A **Flask** app that serves an HTML page with two buttons (e.g., "Yes" and "No" or "Download Cat" and "Clear").
- A **script** that:
  - Uses `anthropic.Anthropic()`
  - Loads the page in a GUI using the `computer` tool
  - Tells Claude to simulate moving the mouse and click each button (no terminal or direct DOM manipulation).

Reference: [Claude's computer tool documentation](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)

---

## 🔧 Tools to Include

- Mouse movement simulation
- Click events triggered via Claude (not programmatically via code)

---

## 📦 Deliverables

Project folder should include:

```
project-folder/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # HTML UI with buttons
├── mouse_demo.py           # Script using Claude to interact with GUI
└── README.md               # Setup and run instructions
```

---

## ✅ Bonus Tip

Use Claude’s `computer` tool for all GUI-related actions to keep the interaction realistic — like a human using a mouse.
