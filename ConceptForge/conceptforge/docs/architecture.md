# Architecture (planned)

```text
Learner selects topic + level
              |
              v
     Streamlit frontend
              |
              v
   Prompt assembly (Week 2+)
              |
              v
 Gemini generative model (Week 2+)
              |
              v
 Pydantic schema validation (Week 3+)
              |
      +-------+-------+
      |               |
  Lesson content   Quiz content
      |               |
      +-------+-------+
              |
       Deterministic scoring
              |
   Misconception / objective mapping
              |
   Targeted GenAI feedback (Week 6+)
              |
       Saved experiment log
```

**Core principle:** Use generative AI for creative explanations and educational exercises, and deterministic Python for scoring, validation and verified numerical examples. Human evaluation remains necessary for educational accuracy.
