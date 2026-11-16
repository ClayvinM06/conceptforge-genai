"""Week 3 generation pathway; Week 2 Markdown records remain unchanged."""

import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from core.lesson_validator import validate_lesson_structure
from core.llm_client import generate_structured, get_model_name
from core.topics import LEVELS, TOPICS
from models.schemas import StructuredLesson

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LESSON_FOLDER = PROJECT_ROOT / "data" / "generated_lessons"


def build_structured_prompt(topic: str, difficulty: str) -> str:
    if topic not in TOPICS:
        raise ValueError(f"Unknown topic: {topic}")
    if difficulty not in LEVELS:
        raise ValueError(f"Unknown difficulty: {difficulty}")

    objectives = "\n".join(f"- {item}" for item in TOPICS[topic]["objectives"])
    topic_rules = ""
    if topic == "Q-learning":
        topic_rules = """
Q-learning-specific accuracy checks:
- Distinguish Q^pi (for a specified policy) from the optimal action value Q*.
- The max next-state action value is a current estimate, not a guaranteed correct future outcome.
- Use a consistent learning-rate convention; alpha=0 means no update, alpha=1 replaces
  the current Q-value with the TD target, which can depend on previously learned estimates.
- Explicitly define s, a, r, gamma, alpha, s-prime and the max over next-state actions.
- Check all numeric arithmetic before returning your worked example.
"""

    return f"""Create ONE original {difficulty.lower()}-level teaching lesson about {topic} for undergraduate STEM learners.

Must explicitly cover these learning objectives:
{objectives}

Content requirements:
- In your JSON output, set the `topic` field to exactly "{topic}".
- In your JSON output, set the `difficulty` field to exactly "{difficulty}".
- Do not add qualifiers such as "undergraduate" to the difficulty field.
- Use accurate technical definitions without misleading simplifications.
- Begin with a short, accessible introduction and explain technical terms clearly.
- Define each mathematical symbol before interpreting its equation.
- Show one correct worked example with givens, intermediate steps and a final answer.
- Include exactly two self-check questions with short reference answers.
- Provide three or more key concepts and two or more takeaways.
- Avoid fabricated citations or claims of independent verification.
- Do not repeat the same sentence across multiple fields.
- Make your explanation appropriate to the selected difficulty level.
- Do not wrap mathematical equations in Markdown dollar delimiters in the equation field.
{topic_rules}
Return the educational content in the required structured response format.
"""


def generate_structured_lesson(topic: str, difficulty: str) -> dict:
    prompt = build_structured_prompt(topic, difficulty)
    lesson = generate_structured(prompt, StructuredLesson)
    validation = validate_lesson_structure(
        lesson, topic, difficulty, len(TOPICS[topic]["objectives"])
    )
    if not validation["structure_passed"]:
        raise ValueError("Structured response failed validation: " + "; ".join(validation["errors"]))

    now = datetime.now(timezone.utc)
    record_id = now.strftime("%Y%m%dT%H%M%SZ") + "_" + uuid4().hex[:8]
    record = {
        "id": record_id,
        "created_at_utc": now.isoformat(),
        "topic": topic,
        "difficulty": difficulty,
        "model": get_model_name(),
        "format": "structured_json",
        "prompt_strategy": "week3_schema_guided",
        "generation_parameters": "SDK/model defaults; application/json with Pydantic response_schema",
        "prompt": prompt,
        "lesson_structured": lesson.model_dump(mode="json"),
        "validation": validation,
        "review_status": "Unverified AI-generated content: human checking required",
    }
    LESSON_FOLDER.mkdir(parents=True, exist_ok=True)
    output_path = LESSON_FOLDER / f"structured_lesson_{record_id}.json"
    output_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    record["saved_to"] = str(output_path.relative_to(PROJECT_ROOT))
    return record


def lesson_to_markdown(lesson: StructuredLesson) -> str:
    sections = [
        f"# {lesson.title}",
        "## Learning objectives",
        *(f"- {item}" for item in lesson.learning_objectives),
        "\n## Introduction\n" + lesson.introduction,
        "## Key concepts",
        *(f"- **{concept.name}:** {concept.explanation}" for concept in lesson.key_concepts),
        "\n## Equation and symbols",
        *(f"- **{definition.symbol}:** {definition.meaning}" for definition in lesson.symbol_definitions),
        f"\n$$\n{lesson.equation_latex}\n$$",
        lesson.equation_explanation,
        "## Worked example",
        lesson.worked_example.problem,
        *(f"- {item}" for item in lesson.worked_example.given_values),
        *(f"{i}. {step}" for i, step in enumerate(lesson.worked_example.solution_steps, 1)),
        f"**Final answer:** {lesson.worked_example.final_answer}",
        "## Key takeaways",
        *(f"- {item}" for item in lesson.key_takeaways),
        "\n## Check your understanding",
        *(f"{i}. {q.question}\n   - Reference answer: {q.expected_answer}" for i, q in enumerate(lesson.self_check_questions, 1)),
    ]
    return "\n\n".join(sections)
