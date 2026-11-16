# Week 3 — Structured lessons and validation

**Project deadline:** 30 January 2027. **Reflective diary RD1:** 20 November 2026.

## Changes

- `models/schemas.py`: Pydantic structures for a complete educational lesson.
- `core/llm_client.py`: retains Week 2 `generate_text` and adds `generate_structured`.
- `core/lesson_validator.py`: local structural checks, **not** a mathematical fact-checker.
- `core/structured_lesson_generator.py`: new prompt, schema-guided request, saved JSON record and Markdown export.
- `app.py`: select the Week 2 Markdown baseline or the new Week 3 structured pathway.
- `tests/test_week3.py`: offline unit tests.

## Apply

Copy all the files from the `conceptforge/` directory of the patch ZIP into your **existing application folder** (the folder containing `app.py`). Replace only same-named files. Do not delete Week 1 or Week 2 work, existing lesson records, journal, `.env`, or `.venv`.

In PowerShell from the app folder:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Choose Q-learning → Beginner. Select **Week 2 — Markdown baseline** to preserve your previous approach, or **Week 3 — Structured JSON** to test the revised approach. Perform one generation with the same topic and difficulty for each. Generated records go in `data/generated_lessons/`.

## Manual evaluation

Compare the outputs against the Week 2 Q-learning problems:
1. Does the learning-rate explanation use a consistent range? Explain `alpha=1` precisely.
2. Does the lesson distinguish a policy's Q-value from the optimal action-value function?
3. Does it call the maximum next-state Q-value an **estimate**, not guaranteed true optimality?
4. Are mathematical symbols defined clearly, and are example calculations correct?
5. Is the explanation suitable for a beginner?

Save your findings in `docs/development_journal.md` and keep the original files. Structured JSON improves presentation and testability, but cannot prove educational accuracy.

## Git

```powershell
git status
git check-ignore .env
git add app.py core/llm_client.py core/lesson_validator.py core/structured_lesson_generator.py models/schemas.py docs/week3_setup.md tests/test_week3.py
git commit -m "Week 3: Add structured lesson generation and validation"
git push
```

If a model rejects the schema or returns unsupported parameters, record the error. Check the selected model's structured-output availability and API quota; do not change the previously working Week 2 pathway.
