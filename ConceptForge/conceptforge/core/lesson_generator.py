# builds educational prompts and preserves first generation record

import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from core.llm_client import generate_text, get_model_name
from core.topics import LEVELS, TOPICS

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LESSON_FOLDER = PROJECT_ROOT / "data" / "generated_lessons"

def build_lesson_prompt(topic: str, difficulty: str) -> str:
    if topic not in TOPICS:
        raise ValueError(f"Unknown topic: {topic}")
    if difficulty not in LEVELS:
        raise ValueError(f"Unknown difficulty: {difficulty}")

    objectives = "\n".join(f"- {item}" for item in TOPICS[topic]["objectives"])
    return f"""You are an educational content author for undergraduate STEM students.

Create ONE original {difficulty.lower()}-level lesson about {topic}.

Learning objectives:
{objectives}

Respond in Markdown with these headings in exactly this order:
# [Specific lesson title]
## Learning objectives
## Explanation
## Worked example
## Key takeaways
## Check your understanding

Requirements:
- Address each learning objective explicitly.
- Make the explanation appropriate for the specified difficulty level.
- Show at least one worked example with clear intermediate steps.
- Explain any symbols before using them in mathematical expressions.
- End with two short self-check questions (no automatic grading yet).
- Prefer accuracy over confidence. Avoid unsupported claims.
- Do not fabricate references, citations, or source material.
- Aim for approximately 450–650 words.
"""

def generate_lesson(topic: str, difficulty: str) -> dict:
    # call gemini, save auditable output record as JSON
    prompt = build_lesson_prompt(topic, difficulty)
    output = generate_text(prompt)

    timestamp = datetime.now(timezone.utc)
    record_id = timestamp.strftime("%Y%m%dT%H%M%SZ") + "_" + uuid4().hex[:8]
    record = {
        "id": record_id,
        "created_at_utc": timestamp.isoformat(),
        "topic": topic,
        "difficulty": difficulty,
        "model": get_model_name(),
        "generation_parameters": "SDK/model defaults (no sampling overrides)",
        "prompt": prompt,
        "lesson_markdown": output,
        "review_status": "Unverified AI-generated content: check facts and calculations",
    }

    LESSON_FOLDER.mkdir(parents=True, exist_ok=True)
    output_path = LESSON_FOLDER / f"lesson_{record_id}.json"
    output_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    record["saved_to"] = str(output_path.relative_to(PROJECT_ROOT))
    return record
