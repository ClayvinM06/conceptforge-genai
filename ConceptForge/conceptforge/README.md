# ConceptForge

**ConceptForge: An Adaptive Generative AI Platform for Personalized STEM Learning**

An ARI3333 Generative AI content production project. The purpose is to generate and evaluate educational learning packs (lessons, worked examples, quizzes, and targeted feedback) using one primary GenAI model, with human review and Python-based verification.

## Current state: Week 1

The Streamlit app is an **interface prototype only**. It does **not** make any model API calls or generate lessons yet. This is intentional.

## Initial content scope

- Q-learning — beginner and advanced
- Backpropagation — beginner and advanced
- Transformer self-attention — beginner and advanced

Each learning pack will eventually include a lesson, worked example, five-question quiz, and targeted feedback.

## Quick start (Windows PowerShell)

From the `conceptforge` directory:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL shown in the terminal (usually `http://localhost:8501`). Stop using `Ctrl+C`.

Using `.venv\Scripts\python.exe` directly avoids PowerShell execution-policy problems associated with activating a virtual environment.

## What is next?

Week 2 connects Gemini using the official `google-genai` SDK; keep your key in a local `.env` file that is ignored by Git. See `docs/project_spec.md` and `docs/week1_checklist.md`.

## Academic responsibilities

- Preserve prompts, model name, settings, output dates and revisions.
- Independently verify AI-generated mathematical solutions and factual claims.
- Distinguish human-authored code and evaluation from AI-produced content.
- Submit three reflective diary entries, the final artefact, the required rationale/critical commentary, and the AI disclosure statement.

**Deadline:** The supplied brief lists January 2026, a past date as of November 2026. The working schedule assumes end of January 2027, **pending verification with the VLE**.
