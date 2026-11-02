# ConceptForge — Week 1 Project Specification

## Working title
ConceptForge: An Adaptive Generative AI Platform for Personalized STEM Learning

## Central objective
Create and critically evaluate original, personalized STEM learning materials produced by a generative language model. Provide an interactive interface supporting lesson generation, quizzes, and rule-based adaptation from student performance.

## Investigative question
How effectively can structured prompting and performance-based feedback improve the accuracy, clarity, and suitability of AI-generated educational content?

## Target audience
Undergraduate students studying introductory and intermediate Artificial Intelligence concepts.

## Input
Selected topic, difficulty level, and (later) quiz responses / missed learning objectives.

## Generated outputs
- Structured educational lesson
- Explained worked example
- Five multiple-choice questions with answer explanations
- Targeted follow-up explanation/practice based on performance

## Curated submission target
Six learning packs: three concepts × two difficulty levels. Curated outputs should be accompanied by prompt records, evaluation criteria, comparison experiments and disclosures.

## Initial subject focus
1. **Q-learning:** state/action values, Bellman-style updates, numerical examples.
2. **Backpropagation:** chain rule, gradient calculation, forward/backward passes.
3. **Transformer self-attention:** queries/keys/values, normalized attention scores, conceptual examples.

## Technology
- Python (application and evaluation)
- Streamlit (interface)
- Gemini through official `google-genai` SDK (primary GenAI technology)
- Pydantic (schema validation)
- Python/SymPy if required later (deterministic math verification)
- JSON/SQLite for saved generations and progress

## Intended evaluation
Compare baseline, structured, and example-guided or adaptive prompting using consistent criteria:
- factual and mathematical accuracy
- clarity and audience suitability
- coverage of learning objectives
- quiz correctness and consistency
- provenance and responsible use

## Constraints / non-goals
No model training, multiple-agent orchestration, authentication, large-scale student analytics or general-purpose tutoring across every subject. This is a generative content coursework project, not a replacement for expert instruction.

## Responsible-AI considerations
Potential hallucinations, accessibility, bias in explanations, copyright and content provenance, data privacy, and over-reliance on AI-generated material. Verify numerical answers independently where possible, and label content as generated.

## Week 1 definition of done
Project specification agreed; folder and Git repository initialized; Python environment created; dependencies install; Streamlit UI runs; first development log started; official January submission date checked with VLE.
