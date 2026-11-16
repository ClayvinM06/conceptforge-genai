"""ConceptForge — Week 3: baseline vs structured lesson generation."""

import json

import streamlit as st

from core.lesson_generator import generate_lesson
from core.structured_lesson_generator import generate_structured_lesson, lesson_to_markdown
from core.topics import LEVELS, TOPICS
from models.schemas import StructuredLesson

st.set_page_config(page_title="ConceptForge | Learning Studio", page_icon="🧠", layout="wide")

st.title("🧠 ConceptForge")
st.caption("An Adaptive Generative AI Platform for Personalized STEM Learning")
st.info("Week 3: Compare the original Markdown generator with structured JSON generation. Quizzes and adaptation are coming later.")

with st.sidebar:
    st.header("Learning settings")
    topic = st.selectbox("Choose a topic", list(TOPICS.keys()))
    difficulty = st.selectbox("Difficulty", LEVELS)
    st.divider()
    st.caption("ARI3333 • Gemini-powered prototype")

st.subheader(f"{topic} — {difficulty}")
st.write(TOPICS[topic]["description"])

lesson_tab, quiz_tab, roadmap_tab = st.tabs(["📘 Learning Studio", "📝 Assessment", "🗓️ Roadmap"])

with lesson_tab:
    st.markdown("#### Learning objectives")
    for objective in TOPICS[topic]["objectives"]:
        st.markdown(f"- {objective}")

    mode = st.radio(
        "Generation method",
        ["Week 2 — Markdown baseline", "Week 3 — Structured JSON"],
        horizontal=True,
        help="Keep the same topic and difficulty to compare the two generation approaches.",
    )
    is_structured = "Structured" in mode

    if st.button("Generate personalized lesson", type="primary"):
        try:
            with st.spinner("Generating a lesson using Gemini..."):
                record = (generate_structured_lesson(topic, difficulty)
                          if is_structured else generate_lesson(topic, difficulty))
                st.session_state["lesson_records"] = st.session_state.get("lesson_records", {})
                st.session_state["lesson_records"][(topic, difficulty, mode)] = record
            st.success("Lesson generated and saved!")
        except Exception as exc:
            st.error(f"Lesson generation failed: {exc}")

    record = st.session_state.get("lesson_records", {}).get((topic, difficulty, mode))
    if record:
        st.divider()
        st.warning("AI-generated educational content: structured formatting does not verify factual accuracy.")
        if is_structured:
            lesson = StructuredLesson.model_validate(record["lesson_structured"])
            st.header(lesson.title)
            st.markdown("#### Introduction")
            st.write(lesson.introduction)
            st.markdown("#### Learning objectives")
            for objective in lesson.learning_objectives:
                st.markdown(f"- {objective}")
            st.markdown("#### Key concepts")
            for concept in lesson.key_concepts:
                st.markdown(f"**{concept.name}** — {concept.explanation}")
            st.markdown("#### Symbols")
            for definition in lesson.symbol_definitions:
                st.markdown(f"- `{definition.symbol}` — {definition.meaning}")
            st.markdown("#### Equation")
            st.latex(lesson.equation_latex.strip().strip("$"))
            st.write(lesson.equation_explanation)
            st.markdown("#### Worked example")
            st.write(lesson.worked_example.problem)
            for given in lesson.worked_example.given_values:
                st.markdown(f"- {given}")
            for i, step in enumerate(lesson.worked_example.solution_steps, 1):
                st.markdown(f"{i}. {step}")
            st.markdown(f"**Final answer:** {lesson.worked_example.final_answer}")
            st.markdown("#### Key takeaways")
            for takeaway in lesson.key_takeaways:
                st.markdown(f"- {takeaway}")
            st.markdown("#### Check your understanding")
            for i, question in enumerate(lesson.self_check_questions, 1):
                st.markdown(f"{i}. {question.question}")
                with st.expander(f"Show reference answer {i}"):
                    st.write(question.expected_answer)
            validation = record["validation"]
            with st.expander("Structural validation (not factual verification)"):
                st.write("Pydantic schema: passed")
                st.write("Required fields: passed")
                for warning in validation["warnings"]:
                    st.warning(warning)
                st.info("Human review is still required, especially for equations and conceptual claims.")
            st.download_button(
                "Download as Markdown",
                data=lesson_to_markdown(lesson),
                file_name=f"conceptforge_{record['id']}.md",
                mime="text/markdown",
            )
            st.download_button(
                "Download structured JSON",
                data=json.dumps(record["lesson_structured"], indent=2, ensure_ascii=False),
                file_name=f"conceptforge_{record['id']}.json",
                mime="application/json",
            )
        else:
            st.markdown(record["lesson_markdown"])
            st.download_button(
                "Download lesson as Markdown",
                data=record["lesson_markdown"],
                file_name=f"conceptforge_{record['id']}.md",
                mime="text/markdown",
            )
        st.caption(f"Model: {record['model']} | Saved to: {record['saved_to']}")
        with st.expander("Generation record — prompt and settings"):
            st.write("Model:", record["model"])
            st.write("Settings:", record["generation_parameters"])
            st.code(record["prompt"], language="text")

with quiz_tab:
    st.markdown("#### Adaptive learning workflow")
    st.write("The model will later generate five multiple-choice questions linked to learning objectives.")
    st.write("Python will score answers and request targeted explanations for missed objectives.")
    st.button("Generate five-question quiz", disabled=True, help="Scheduled for a later week")

with roadmap_tab:
    st.markdown("#### Key milestones")
    st.table([
        {"Phase": "Week 1", "Deliverable": "Specification, repository and UI prototype"},
        {"Phase": "Week 2", "Deliverable": "First live Gemini-generated lesson"},
        {"Phase": "Week 3", "Deliverable": "Pydantic schema and structured lesson experiments"},
        {"Phase": "Weeks 4–7", "Deliverable": "Quiz generation, validation and adaptive feedback"},
        {"Phase": "Weeks 8–11", "Deliverable": "Evaluation and curated learning packs"},
        {"Phase": "Weeks 12–13", "Deliverable": "Final portfolio and submission by 30 Jan 2027"},
    ])

st.divider()
st.caption("Model-generated content is unverified until independently checked.")
