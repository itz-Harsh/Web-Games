 # 🎮 Web Games — Tic‑Tac‑Toe & Rock‑Paper‑Scissors

A tiny, fun collection of browser games with a simple voice backend for RPS. Play in-browser, or use the included Flask service to speak your move.

✨ What’s inside
- 📄 `index.html` — Landing page that links the games
- 🎨 `styles.css` — Main site styles
- ❌⭕ `games/tic-tac-toe.html` + `games/style-ttt.css` — Tic‑Tac‑Toe (vs Computer or 2‑player)
- ✋✌️ `games/rock-paper-scissor.html` + `games/style-rps.css` — Rock‑Paper‑Scissors (click or voice)
- 🧠 `app.py` — Small Flask voice backend (records mic → recognizes rock/paper/scissors)

🚀 Quick start (Windows PowerShell)

1) Serve the static site from the project root:

```powershell
cd "f:\Codes\PROJECTS\Web-Games"
python -m http.server 8000
```

Open http://localhost:8000 in your browser and click a game.

2) (Optional) Start the voice backend (for RPS voice button):

```powershell
cd "f:\Codes\PROJECTS\Web-Games"
python app.py
```

The backend runs on port `5000` and exposes `/listen` returning JSON like `{ "choice": "rock" }`.

📦 Python dependencies (for `app.py`)
- Flask
- Flask-CORS
- SpeechRecognition
- PyAudio (or alternative)

Recommended: use a venv then install packages.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install Flask Flask-Cors SpeechRecognition PyAudio
```

Tip: if `PyAudio` is hard to install on Windows, try `pip install pipwin` then `pipwin install pyaudio`.

🛠 Notes & troubleshooting
- 🔊 Voice: the RPS page calls `http://127.0.0.1:5000/listen`. Make sure `app.py` is running and the mic is available.
- 🎯 No voice? Click the choice tiles in the RPS page — voice is optional.
- 🖼 Images not showing on the landing page? Serve the site via HTTP (see step 1); don’t use `file://`.

🌟 Nice extras you can add
- Replace alerts with an on‑page status UI (improves UX)
- Add persistent scores using localStorage
- Improve Tic‑Tac‑Toe AI (minimax) or add animated effects

—
If you want, I can also add a `requirements.txt`, or a PowerShell script that starts both the static server and the Flask backend in two terminals. Which would you like?
