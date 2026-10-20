import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()
app = Flask(__name__)

# Set GEMINI_API_KEY in your .env file. Never put API keys in frontend JavaScript.
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

def generate_study_content(topic_or_text, task):
    if not API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured. Add it to your .env file.")
    client = genai.Client(api_key=API_KEY)

    instructions = {
        "notes": "Create clear, well-organized study notes with headings, key terms, and a short summary. Use simple language. Do not invent facts.",
        "summary": "Summarize the provided topic or material in concise, easy-to-understand language. Preserve important points and define key terms.",
        "questions": "Create 8 important study questions from the provided topic or material. Include a mix of short-answer and conceptual questions, then provide a separate answer key.",
        "quiz": "Create 5 multiple-choice questions based on the provided topic or material. Each question must have four options (A-D), identify the correct answer, and briefly explain why it is correct."
    }
    prompt = f"""You are StudySpark AI, a careful study assistant.
Task: {instructions[task]}
Student input:
{topic_or_text}

Requirements:
- Be educational, clear, and accurate.
- If the input is too vague, state your assumption.
- If the user pasted source material, prioritize that material.
- For important factual uncertainty, say that the student should verify it with their course materials.
- Format the answer using readable headings and bullet points.
"""
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return response.text or "The AI returned an empty response. Please try again."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    content = (data.get("content") or "").strip()
    task = data.get("task", "notes")
    if len(content) < 3:
        return jsonify(error="Please enter a topic or paste some study material."), 400
    if len(content) > 12000:
        return jsonify(error="Please keep your input under 12,000 characters for this prototype."), 400
    if task not in {"notes", "summary", "questions", "quiz"}:
        return jsonify(error="Please choose a valid study task."), 400
    try:
        result = generate_study_content(content, task)
        return jsonify(result=result)
    except Exception as exc:
        # Return a user-friendly message; do not expose secrets or internal details.
        message = str(exc)
        if "GEMINI_API_KEY" in message:
            safe_message = message
        else:
            safe_message = "The AI service could not complete the request. Check your API key, internet connection, quota, and model configuration, then try again."
        app.logger.exception("Generation failed")
        return jsonify(error=safe_message), 502

if __name__ == "__main__":
    # Local development only. Use a production WSGI server for public deployment.
    app.run(debug=True)
