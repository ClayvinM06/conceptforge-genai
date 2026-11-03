import streamlit as st

from core.lesson_generator import generate_lesson
from core.topics import LEVELS, TOPICS

st.set_page_config(page_title="ConceptForge | Learning Studio", page_icon="🧠", layout="wide")

st.title("ConceptForge")
st.caption("An Adaptive Generative AI Platform for Personalized STEM Learning")
st.info("Week 2: AI lesson generation is enabled. Quizzes and adaptation arrive in later weeks.")

with st.sidebar:
    st.header("Learning settings")
    topic = st.selectbox("Choose a topic", list(TOPICS.keys()))
    difficulty = st.selectbox("Difficulty", LEVELS)
    st.divider()
    st.caption("ARI3333 • Gemini-powered prototype")

st.subheader(f"{topic} — {difficulty}")
st.write(TOPICS[topic]["description"])

lesson_tab, quiz_tab, roadmap_tab = st.tabs(
    ["📘 Learning Studio", "📝 Assessment", "🗓️ Roadmap"]
)

with lesson_tab:
    st.markdown("#### Learning objectives")
    for objective in TOPICS[topic]["objectives"]:
        st.markdown(f"- {objective}")

    if st.button("Generate personalized lesson", type="primary"):
        try:
            with st.spinner("Generating a lesson using Gemini..."):
                st.session_state["lesson_record"] = generate_lesson(topic, difficulty)
            st.success("Lesson generated and saved!")
        except Exception as exc:
            st.error(f"Lesson generation failed: {exc}")

    record = st.session_state.get("lesson_record")
    if record and record["topic"] == topic and record["difficulty"] == difficulty:
        st.divider()
        st.warning("AI-generated lesson: verify technical claims and calculations before use.")
        st.markdown(record["lesson_markdown"])
        st.caption(f"Model: {record['model']} | Saved to: {record['saved_to']}")
        st.download_button(
            "Download lesson as Markdown",
            data=record["lesson_markdown"],
            file_name=f"conceptforge_{record['id']}.md",
            mime="text/markdown",
        )
        with st.expander("Generation record — prompt and settings"):
            st.write("Model:", record["model"])
            st.write("Settings:", record["generation_parameters"])
            st.code(record["prompt"], language="text")

with quiz_tab:
    st.markdown("#### Adaptive learning workflow")
    st.write("The model will generate five multiple-choice questions linked to the topic objectives.")
    st.write("Python will score questions and request targeted explanations for missed objectives.")
    st.button("Generate five-question quiz", disabled=True, help="Scheduled for later development")

with roadmap_tab:
    st.markdown("#### Key milestones")
    st.table([
        {"Phase": "Week 1", "Deliverable": "Specification, repository and UI prototype"},
        {"Phase": "Week 2", "Deliverable": "First live Gemini-generated lesson"},
        {"Phase": "Weeks 3–7", "Deliverable": "Structured content, quizzes and adaptive feedback"},
        {"Phase": "Weeks 8–11", "Deliverable": "Prompt experiments and curated learning packs"},
        {"Phase": "Weeks 12–13", "Deliverable": "Written portfolio, testing and submission"},
    ])

st.divider()
st.caption("ConceptForge is a prototype; generated educational content is not automatically verified.")
