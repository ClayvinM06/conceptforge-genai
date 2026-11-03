# Week 2 — Gemini integration

**Confirmed ARI3333 submission deadline: 30 January 2027.**

## Apply the upgrade

Copy the following files from the upgrade archive into your **existing** ConceptForge application folder (where `app.py` currently lives), replacing `app.py` and `.env.example`:

- `app.py`
- `core/llm_client.py`
- `core/lesson_generator.py`
- `.env.example`
- `docs/week2_setup.md`

Do **not** delete your existing project directory, journal or Git history.

## Create the API key

Open https://aistudio.google.com/apikey and create a dedicated key for ConceptForge. In the app folder, create `.env` with:

```dotenv
GEMINI_API_KEY=replace_with_your_real_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

`.gitignore` already excludes `.env`. Do not screenshot, paste, or commit your key.

## Run on Windows (PowerShell)

In the folder containing `app.py`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Select Q-learning → Beginner and click **Generate personalized lesson**. Generation results should appear in the UI and be stored in `data/generated_lessons/` as JSON. The lesson content is not automatically fact-checked yet; check its technical claims before citing it in your coursework.

## Save progress to GitHub

```powershell
git status
git add app.py core/llm_client.py core/lesson_generator.py .env.example docs/week2_setup.md
git commit -m "Week 2: Connect Gemini and generate educational lessons"
git push
```

**Do not include `.env` in the commit.** Generated records can be curated for your portfolio after manual review. Keep API keys and private data out of prompts and logs.

## Problems

- Missing key: confirm `.env` sits beside `app.py`, not in the outer GitHub repository directory.
- 404/model not available: check API model access in AI Studio and adjust `GEMINI_MODEL` to a model your key can use.
- 429/rate limit: review free-tier quotas in AI Studio; retry after your quota resets.
- Bad model outputs: expected at this stage; preserve the record and critique it during evaluation.
