# ConceptForge — Week 3 Comparison Record

**Date:**
**Topic:** Q-learning
**Difficulty:** Beginner
**Gemini model:**

## Evidence files

- Week 2 Markdown baseline record: `lesson_20261103T104927Z_7242c5cb.json` (the original Week 2 sample; verify your local filename)
- Week 3 structured JSON record:

## Baseline observations (from first reviewed Q-learning lesson)

- Numerical Q-learning worked example produced **56.5** and its arithmetic was verified.
- The learning-rate description excluded alpha=0 in its stated range but discussed it immediately afterward.
- The statement about alpha=1 being based only on new information was too broad.
- The Q-function description did not carefully distinguish a policy's action values from the optimal function.
- The maximum next-state Q-value was presented like an assured best future path rather than an estimate.
- Mathematical symbols were defined after first presenting the equation, despite the original prompt.

## Structured generation observations

Write down the exact phrases from your new lesson. Do not fill these sections before testing.

- Learning-rate range and alpha=1 explanation:
- Policy-specific vs optimal Q-function:
- Estimated (not guaranteed) future Q-value:
- Order and clarity of mathematical symbol definitions:
- Worked-example arithmetic (show independent calculation):
- Other problems identified:

## Comparative scoring (manual; 1 = weak, 5 = strong)

| Criterion | Week 2 Markdown | Week 3 Structured | Evidence / notes |
|---|---:|---:|---|
| Conceptual accuracy | | | |
| Numerical accuracy | | | |
| Completeness | | | |
| Clarity for beginners | | | |
| Prompt adherence | | | |
| Ease of automated parsing | | | |

## Interpretation

- What improved?
- What did not improve?
- What new issues were introduced?
- What evidence justifies each conclusion?
- Which corrections require independent human assessment?

**Experimental limitation:** The Week 3 test changes both the output schema and some prompt wording. If quality improves, you cannot attribute the improvement *solely* to schema enforcement. Treat this as a comparison between the two complete generation workflows, or run an additional controlled experiment later.

**Ethical note:** Do not equate valid JSON with correct educational content. AI-produced explanations need human fact-checking before being used as authoritative teaching material.
