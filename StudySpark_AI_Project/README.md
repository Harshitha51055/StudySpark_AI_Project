# StudySpark AI — Study Notes and Quiz Generator

A beginner-friendly GenAI web application for generating study notes, summaries, important questions, and multiple-choice quizzes.

## Features
- Four study tasks: notes, summary, questions, and quiz
- Responsive HTML/CSS/JavaScript interface
- Flask backend with input validation and error handling
- Gemini API integration through the official `google-genai` Python SDK
- Copy generated output
- API key kept in an environment file, not frontend JavaScript

## Requirements
- Python 3.10+ (use a currently supported Python version)
- Internet access
- A Gemini API key with access to the selected model

## Setup (Windows PowerShell)
1. Extract this ZIP and open the `StudySpark_AI_Project` folder in VS Code.
2. Open a terminal in this folder.
3. Create a virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt and run `.venv\\Scripts\\activate.bat`.
4. Install packages:
   ```powershell
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to a new file named `.env`.
6. Open `.env` and replace `put_your_api_key_here` with your own API key. Do not share the `.env` file or commit it to Git.
7. Run:
   ```powershell
   python app.py
   ```
8. Open `http://127.0.0.1:5000` in your browser.

## Test cases
- Enter a topic such as `Database normalization` and generate notes.
- Select Summary, Important questions, and Practice quiz in separate attempts.
- Submit empty input and confirm that a validation message appears.
- Test a longer input and check that results remain readable.
- Temporarily remove the API key and confirm that a helpful configuration message appears.

## Architecture
Student → Browser UI (HTML/CSS/JS) → Flask `/generate` endpoint → Prompt construction → Gemini API → Flask response → Result displayed in browser.

## Important
- This project requires an API key and internet access for real AI output.
- Model names, API availability, quotas, and billing can change. Check the provider's current documentation.
- The current project is a local prototype, not a production-hardened public service.
- The report template requires actual screenshots. Run the app and capture your own screenshots before final submission.
