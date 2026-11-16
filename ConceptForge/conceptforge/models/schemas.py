"""Typed educational content schema, independent from the Streamlit UI."""

from typing import Literal

from pydantic import BaseModel, Field, field_validator


class KeyConcept(BaseModel):
    name: str = Field(description="Name of a technical concept")
    explanation: str = Field(description="Audience-appropriate explanation")


class SymbolDefinition(BaseModel):
    symbol: str = Field(description="Mathematical symbol, optionally in LaTeX")
    meaning: str = Field(description="Meaning in plain language")


class WorkedExample(BaseModel):
    problem: str = Field(description="Original illustrative problem")
    given_values: list[str] = Field(description="Given inputs and units if relevant")
    solution_steps: list[str] = Field(description="Reasoned intermediate calculation steps")
    final_answer: str = Field(description="Final calculated or conceptual answer")


class SelfCheckQuestion(BaseModel):
    question: str = Field(description="A short comprehension question")
    expected_answer: str = Field(description="Reference answer; not yet independently verified")


class StructuredLesson(BaseModel):
    topic: str
    difficulty: Literal["Beginner", "Advanced"]

    @field_validator("difficulty", mode="before")
    @classmethod
    def normalize_difficulty(cls, value):
        if isinstance(value, str):
            aliases = {
                "beginner": "Beginner",
                "beginner undergraduate": "Beginner",
                "advanced": "Advanced",
                "advanced undergraduate": "Advanced",
            }
            return aliases.get(value.strip().casefold(), value)
        return value

    title: str
    introduction: str
    learning_objectives: list[str]
    key_concepts: list[KeyConcept]
    symbol_definitions: list[SymbolDefinition]
    equation_latex: str = Field(description="One key equation, without dollar delimiters")
    equation_explanation: str
    worked_example: WorkedExample
    key_takeaways: list[str]
    self_check_questions: list[SelfCheckQuestion]
