"""ConceptForge — Week 1 interface prototype (no AI API calls yet)."""

import streamlit as st

from core.topics import TOPICS, LEVELS

st.set_page_config(page_title="ConceptForge | Learning Studio", page_icon="🧠", layout="wide")

st.title("🧠 ConceptForge")
st.caption("An Adaptive Generative AI Platform for Personalized STEM Learning")
st.info("Week 1 prototype: AI lesson generation, quizzes and adaptation will be implemented in later weeks.")

with st.sidebar:
    st.header("Learning settings")
    topic = st.selectbox("Choose a topic", list(TOPICS.keys()))
    difficulty = st.selectbox("Difficulty", LEVELS)
    st.divider()
    st.caption("ARI3333 • Development prototype")

st.subheader(f"{topic} — {difficulty}")
st.write(TOPICS[topic]["description"])

lesson_tab, quiz_tab, roadmap_tab = st.tabs(["📘 Learning Studio", "📝 Assessment", "🗓️ Roadmap"])

with lesson_tab:
    st.markdown("#### Learning objectives")
    for objective in TOPICS[topic]["objectives"]:
        st.markdown(f"- {objective}")
    st.write("**Planned output:** a generated lesson, one worked example, and cited model settings/prompt records.")
    st.button("Generate personalized lesson", disabled=True, help="Scheduled for Week 2 onward")

with quiz_tab:
    st.markdown("#### Adaptive learning workflow")
    st.write("The model will generate five multiple-choice questions linked to the topic objectives.")
    st.write("Python will score objective questions and request targeted explanations for missed objectives.")
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
st.caption("The current screen is a UI scaffold, not an AI-generated output or a completed tutoring system.")
