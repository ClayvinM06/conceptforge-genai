"""Offline tests: no API key and no Gemini calls required."""

import unittest

from core.lesson_validator import validate_lesson_structure
from models.schemas import StructuredLesson


class TestWeek3(unittest.TestCase):
    def build_lesson(self):
        return StructuredLesson.model_validate({
            "topic": "Q-learning",
            "difficulty": "Beginner",
            "title": "Introduction to Q-learning",
            "introduction": "An agent learns action values from experience.",
            "learning_objectives": ["Explain states", "Interpret updates", "Calculate an update"],
            "key_concepts": [
                {"name": "state", "explanation": "Environment situation"},
                {"name": "action", "explanation": "Possible choice"},
                {"name": "reward", "explanation": "Feedback"},
            ],
            "symbol_definitions": [
                {"symbol": "alpha", "meaning": "learning rate"},
                {"symbol": "gamma", "meaning": "discount factor"},
            ],
            "equation_latex": "Q_{new}=Q+\\alpha(r+\\gamma Q'-Q)",
            "equation_explanation": "The update combines a current value with a target.",
            "worked_example": {
                "problem": "Compute the update.",
                "given_values": ["Q=40", "alpha=0.5", "r=10", "gamma=0.9", "max next Q=70"],
                "solution_steps": ["0.9*70=63", "40+0.5*(10+63-40)=56.5"],
                "final_answer": "56.5",
            },
            "key_takeaways": ["Q-values represent returns", "Rewards guide learning"],
            "self_check_questions": [
                {"question": "What is a reward?", "expected_answer": "Feedback"},
                {"question": "What is alpha?", "expected_answer": "Learning rate"},
            ],
        })

    def test_valid_content_has_no_structure_errors(self):
        result = validate_lesson_structure(self.build_lesson(), "Q-learning", "Beginner", 3)
        self.assertTrue(result["structure_passed"])
        self.assertFalse(result["factual_accuracy_verified"])

    def test_difficulty_mismatch_is_detected(self):
        result = validate_lesson_structure(self.build_lesson(), "Q-learning", "Advanced", 3)
        self.assertFalse(result["structure_passed"])
        self.assertTrue(result["errors"])

    def test_beginner_undergraduate_is_normalized(self):
        record = self.build_lesson().model_dump()
        record["difficulty"] = "Beginner undergraduate"
        lesson = StructuredLesson.model_validate(record)
        self.assertEqual(lesson.difficulty, "Beginner")
        result = validate_lesson_structure(lesson, "Q-learning", "Beginner", 3)
        self.assertTrue(result["structure_passed"])

    def test_advanced_undergraduate_remains_wrong_for_beginner(self):
        record = self.build_lesson().model_dump()
        record["difficulty"] = "Advanced undergraduate"
        lesson = StructuredLesson.model_validate(record)
        result = validate_lesson_structure(lesson, "Q-learning", "Beginner", 3)
        self.assertFalse(result["structure_passed"])

    def test_missing_question_is_warned_about(self):
        lesson = self.build_lesson()
        lesson.self_check_questions.pop()
        result = validate_lesson_structure(lesson, "Q-learning", "Beginner", 3)
        self.assertTrue(result["warnings"])

    def test_required_field_rejected_by_pydantic(self):
        record = self.build_lesson().model_dump()
        del record["worked_example"]
        with self.assertRaises(Exception):
            StructuredLesson.model_validate(record)


if __name__ == "__main__":
    unittest.main()
