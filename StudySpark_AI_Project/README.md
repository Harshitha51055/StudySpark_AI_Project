# StudySpark AI — Study Notes and Quiz Generator

StudySpark AI is a Generative AI-powered web application that helps students prepare learning materials from a topic or study text they enter. It uses Google's Gemini AI to generate study notes, summaries, important questions with answers, and multiple-choice quizzes.

## Features

- **Study Notes:** Generate organized notes from the provided topic or text.
- **Summaries:** Convert study material into concise summaries for quick revision.
- **Important Questions:** Generate relevant questions with answers to support exam preparation.
- **MCQ Quizzes:** Create multiple-choice practice questions with an answer key.
- **Simple Web Interface:** Enter or paste study material, select the required output, and view the generated content.
- **AI-Powered Generation:** Uses the Gemini API to generate learning resources dynamically.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python and Flask
- **Generative AI:** Google Gemini API
- **Configuration:** Python dotenv (`.env` file)
- **Dependency Management:** pip and `requirements.txt`

## How It Works

1. The user enters a topic or pastes study material into the application.
2. The user selects the required output, such as notes, a summary, important questions, or an MCQ quiz.
3. The Flask backend receives the request.
4. The application sends the relevant prompt to the Gemini API.
5. Gemini generates the requested learning content.
6. The generated result is displayed in the web interface for the user to read and use for revision.

## Project Structure

```text
StudySpark_AI_Project/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

The `.env` file and virtual environment are kept locally and should not be uploaded to GitHub.

## Requirements

- Python installed on your computer
- A Google Gemini API key
- Internet access for API requests
- pip for installing Python dependencies

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd StudySpark_AI_Project
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Create and activate a virtual environment (recommended)

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local file named `.env` in the same directory as `app.py`. Add your own Gemini API key and the model configured for your application:

```env
GEMINI_API_KEY=your_actual_api_key
GEMINI_MODEL=gemini-3.8-flash
```

Replace the placeholder API key with your own key. Use the model identifier supported by your Gemini API account and application code.

**Security:** Never upload your real `.env` file or expose your API key in screenshots, source code, or public commits. The `.env.example` file should contain placeholders only.

### 5. Run the application

```bash
python app.py
```

Open the local address shown in the terminal. For the current local setup, this is:

```text
http://127.0.0.1:5000
```

## Current Limitations

- The current application accepts a topic or pasted text; file upload and automatic document extraction are not implemented.
- Generated content depends on the quality of the input and the AI response.
- Gemini API access requires a valid API key, an available model, and an internet connection.
- API usage may be subject to provider quotas and limits.
- AI-generated answers should be reviewed for accuracy before being used for academic work.

## Future Enhancements

- Upload PDF, DOCX, and TXT study materials.
- Add flashcards and additional quiz formats.
- Allow users to download generated notes.
- Add user accounts and save previous study sessions.
- Support additional languages and adjustable difficulty levels.
- Deploy the application to a cloud hosting platform.

## Purpose

StudySpark AI aims to make study preparation more convenient by turning user-provided topics and study material into organized learning resources. It supports revision and self-learning through AI-generated notes, summaries, questions, and quizzes.

## License

A license has not yet been specified for this project.
