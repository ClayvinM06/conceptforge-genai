"""Structural checks only. Passing does NOT imply factual accuracy."""

from models.schemas import StructuredLesson


def validate_lesson_structure(lesson: StructuredLesson, topic: str, difficulty: str, expected_objectives: int) -> dict:
    warnings = []
    errors = []

    if lesson.topic.strip().casefold() != topic.strip().casefold():
        errors.append(f"Wrong topic: received {lesson.topic!r}")
    if lesson.difficulty.strip().casefold() != difficulty.strip().casefold():
        errors.append(f"Wrong difficulty: received {lesson.difficulty!r}")

    for field in ("title", "introduction", "equation_latex", "equation_explanation"):
        if not getattr(lesson, field).strip():
            errors.append(f"Missing or blank field: {field}")

    if len(lesson.learning_objectives) != expected_objectives:
        warnings.append(f"Expected {expected_objectives} learning objectives, received {len(lesson.learning_objectives)}")
    if len(lesson.key_concepts) < 3:
        warnings.append("Fewer than three key concepts")
    if len(lesson.symbol_definitions) < 2:
        warnings.append("Equation symbols may not be adequately defined")
    if len(lesson.worked_example.solution_steps) < 2:
        warnings.append("Worked example has fewer than two calculation steps")
    if len(lesson.self_check_questions) != 2:
        warnings.append(f"Expected 2 self-check questions, received {len(lesson.self_check_questions)}")

    for name, values in (
        ("learning_objectives", lesson.learning_objectives),
        ("key_takeaways", lesson.key_takeaways),
        ("solution_steps", lesson.worked_example.solution_steps),
    ):
        if not values or any(not value.strip() for value in values):
            errors.append(f"Missing or blank content in {name}")

    if not lesson.worked_example.problem.strip() or not lesson.worked_example.final_answer.strip():
        errors.append("Worked example is incomplete")

    return {
        "schema_valid": True,
        "structure_passed": not errors,
        "errors": errors,
        "warnings": warnings,
        "factual_accuracy_verified": False,
        "manual_review_required": True,
    }
