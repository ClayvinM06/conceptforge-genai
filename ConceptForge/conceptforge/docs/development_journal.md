# ConceptForge — Development Notes

This is a private evidence log used to **write** the three 300–400-word VLE reflective diary entries. Do not fabricate observations: fill it in after real work.

## Week 1 — 2–8 November 2026

**Conceptual understanding:**
- What concepts from lectures or readings relate to the planned system?

During the first week, I focused on defining the objectives and general architecture of ConceptForge, an educational platform designed to generate personalised learning material using Generative AI tools.

The project will utilise a Transformer-based Large Language Model (LLM) to generate explanations, worked examples, and assessment questions. A key consideration was understanding the distinction between generating educational content and ensuring factual accuracy. Although LLMs can produce coherent explanations, their outputs may not necessarily be correct, notably when handling mathematical concepts.

I devided that ConceptForge should combine generative capabilities with deterministic Python-based validation and assessment mechanisms.

**Practical engagement:**
- What did I set up, test, or prototype? Were the environment and Streamlit interface successful?

I setup the initial development environment using Python, GitHub and Streamlit.

I launched a working Streamlit prototype containing topic selection, difficulty settings, learning objectives and separate interface sections for learning, assessment and development milestones.

Three initial learning topics were selected: Q-learning, backpropagation, and Transformer self-attention. These subjects provide opportunities to investigate conceptual explanations and mathematical reasoning. 

I also initialised a GitHub repository and successfully uploaded the initial project structure to GitHub, establishing version control for subsequent development. 

**Methodological Learning and Challenges:**
- What errors, incorrect assumptions or design trade-offs arose? How did I investigate or address them?

One technical challenge I encountered involved configuring Git on Windows. Initially, the PowerShell couldn't recognise the **git** command, preventing repository initialisation. After resolving the Git configuration issue, I successfully created and pushed the initial commit. 

This challenge reinforced the importance of establising a reliable development environment before implementing more functionality. 

Another important design decision was to separate the user interface, content generation, validation and adaptive learning components. This modular approach should simplify debugging and allow individual components to be tested independently. 

**Ethical / societal considerations:**
- What could go wrong if students rely on generated lessons?

A significant concern identified during planning was the possibility of AI-generated educational misinformation. Incorrect explanations or mathematical solutions could impose a negative effect on the learner's understanding. 

To address this, I intend to introduce a structured output validation, independent mathematical verification where feasible, and systematic evaluation of generated content. 

The project will also consider responsible AI use, particularly the importance of maintaining human oversight rather than treating generated educational material as automatically trustworthy. 

**Evidence:**
- Commit ID:
- Screenshot or file:
- Date:

**Reflection:**
- What did I learn and what will I change next week?

This week highlighted that developing a reliable educational AI application requires more than integrating a generative model. Careful system design, validation and critical evaluation are equally important. 

The next stage in development will involve integrating the Gemini API and generating the first educational lesson, allowing me to begin evaluating the model's actual capabilities and limitations. 

## Future entry milestones
- Entry 1 — by approximately 22 Nov: theory and initial text-generation experiments.
- Entry 2 — by approximately 6 Dec: prompting, structured output and quizzes.
- Entry 3 — by approximately 20 Dec: adaptation, validation and ethics.

The above are planning targets, not official VLE dates.
