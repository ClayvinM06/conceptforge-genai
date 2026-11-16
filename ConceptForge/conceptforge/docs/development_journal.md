# ConceptForge — Development Notes

This is a private evidence log used to **write** the three 300–400-word VLE reflective diary entries. Do not fabricate observations: fill it in after real work.

## Week 1 — 2–8 November 2026

**Conceptual understanding:**

During the first week, I focused on defining the objectives and general architecture of ConceptForge, an educational platform designed to generate personalised learning material using Generative AI tools.

The project will utilise a Transformer-based Large Language Model (LLM) to generate explanations, worked examples, and assessment questions. A key consideration was understanding the distinction between generating educational content and ensuring factual accuracy. Although LLMs can produce coherent explanations, their outputs may not necessarily be correct, notably when handling mathematical concepts.

I devided that ConceptForge should combine generative capabilities with deterministic Python-based validation and assessment mechanisms.

**Practical engagement:**

I setup the initial development environment using Python, GitHub and Streamlit.

I launched a working Streamlit prototype containing topic selection, difficulty settings, learning objectives and separate interface sections for learning, assessment and development milestones.

Three initial learning topics were selected: Q-learning, backpropagation, and Transformer self-attention. These subjects provide opportunities to investigate conceptual explanations and mathematical reasoning. 

I also initialised a GitHub repository and successfully uploaded the initial project structure to GitHub, establishing version control for subsequent development. 

**Methodological Learning and Challenges:**

One technical challenge I encountered involved configuring Git on Windows. Initially, the PowerShell couldn't recognise the **git** command, preventing repository initialisation. After resolving the Git configuration issue, I successfully created and pushed the initial commit. 

This challenge reinforced the importance of establising a reliable development environment before implementing more functionality. 

Another important design decision was to separate the user interface, content generation, validation and adaptive learning components. This modular approach should simplify debugging and allow individual components to be tested independently. 

**Ethical / societal considerations:**

A significant concern identified during planning was the possibility of AI-generated educational misinformation. Incorrect explanations or mathematical solutions could impose a negative effect on the learner's understanding. 

To address this, I intend to introduce a structured output validation, independent mathematical verification where feasible, and systematic evaluation of generated content. 

The project will also consider responsible AI use, particularly the importance of maintaining human oversight rather than treating generated educational material as automatically trustworthy. 

**Evidence:**
- Commit ID:
- Screenshot or file:
- Date:

**Reflection and next steps:**

This week highlighted that developing a reliable educational AI application requires more than integrating a generative model. Careful system design, validation and critical evaluation are equally important. 

The next stage in development will involve integrating the Gemini API and generating the first educational lesson, allowing me to begin evaluating the model's actual capabilities and limitations. 

## Week 2 — 9–15 November 2026

**Conceptual understanding:**

During the second week of development, I focused on integrating an LLM into my project to enable the generation of personalised educational content. This provided an opportunity to explore how transformer-based generative models can produce structured explanations based on specific instructions and learning objectives.

An important concept I explored was prompt engineering. I recognised that providing explicit instructions regarding content structure, difficulty level, and learning obectives allows greater control over the generated material. However, I also learned that producing well-structured content doesn't necessarily guarantee factual accuracy.

**Practical engagement:**

I successfully integrated Google Gemini's API into the existing Python and Streamlit architecture, enabling ConceptForge to generate educational lessons dynamically.

I implemented a lesson-generation component that constructs prompt according to the selected topic and difficulty level. The generated responses follow a predefined markdown structure containing learning objectives, explanations, worked examples, key takeaways and self assessment questions. 

I also implemented functionality to save the generated lessons as JSON files, including the original prompt, model information, generation settings, output and timestamp. This will support reproducibiltiy and future experimentation.

The first successful generation involved a beginner-level Q-learning lesson. I also tested the generation functionality across the other learning configurations and topics. 

**Methodological Learning and Challenges:**

An important challenge involved evaluating whether the generated educational content was technically accurate. 

During the evaluation of the Q-learning lesson, the model successfully demonstrated the update equation and produces a mathematically correct result of 56.5. However, I identified several conceptual imprecisions. These included an inconsistent definition of the learning rate's valid range, an oversimplified interpretation of the Q-function, and a description of estimated future Q-values as thoguh they represented guaranteed optimal outcomes.

Although these issues did not affect the mathematical calculation, they highlighted an important limitation of Generative AI in educational applications. A response can be mathematically correct and well structured while still containing potentially misleading conceptual explanations.

Consequently, I recognised the importance of improving prompt specificity and introducing systematic content validation. These observations will guide the development of more structured generation and evaluation mechanisms in the subsequent weeks. 

**Ethical / societal considerations:**

A significant concern identified during experimentation was the reliability of AI-generated educational material. Students may interpret confidently presented explanations as factual, potentially reinforcing misunderstandings.

This reinforced the importance of incorporating independent validation and maintaining human oversight throughout the content-generation process.

I also recognized the need to document prompts, generation settings and subsequent modifications to ensure transparency regarding the role of Generative AI.

**Reflection and next steps:**

This week's progress demonstrated the practical capabilities of LLMs in educational content production while highlighting their limitations.

The next development stage will focus on implementing structured JSON generation using Pydantic schemas, improving output consistency and introducing validation mechanisms.

These improvements should provide a more reliable foundation for the future quiz-generation and adaptive learning components.

## Week 3 — 16–22 November 2026

**Conceptual understanding:**

During the third week of development, I focused on improving the structure, consistency and reliability of AI-generated educational content. Following the initial Gemini integration, I recognized that generating lessons in Markdown provided limited control over individual content components.

I explored structured output generation using JSON and Pydantic schemas. This approach allows specific requirements to be imposed on generated lessons, including predefined fields for explanations, mathematical symbols, worked examples and assessment questions.

An important distinction I learned was that structural validation does not guarantee factual accuracy. Although a generated response may satisfy all predefined schema requirements, its explanations and calculations may still contain inaccuracies.

**Practical engagement:**

I extended ConceptForge by implementing structured JSON generation using the Gemini API. I introduced Pydantic models to define the expected lesson format and developed validation mechanisms to check required fields, difficulty levels and content completeness.

The Streamlit interface was updated to support both the original Week 2 Markdown generation method and the new structured approach, allowing comparisons between them.

I successfully generated a structured beginner-level Q-learning lesson containing learning objectives, key concepts, mathematical definitions, a worked example and self-assessment questions.

The generated worked example produced an updated Q-value of 16.0, which I independently verified as mathematically correct.

I also implemented and executed six automated unit tests, all of which passed successfully.

**Methodological Learning and Challenges:**

One significant challenge occurred when Gemini returned the difficulty value "Beginner undergraduate" instead of the expected "Beginner". Although semantically appropriate, this caused the strict validation system to reject the response.

To resolve this, I refined the generation instructions and introduced difficulty normalization while preserving validation against genuinely incorrect difficulty levels.

This demonstrated the importance of balancing strict programmatic constraints with the variability of generative model outputs.

Comparing the Week 2 and Week 3 lessons also revealed improvements in content organization and some conceptual explanations. However, certain imprecisions remained, particularly regarding the Q-function and discount factor.

**Ethical / societal considerations:**

This week's experiments highlighted the risks associated with relying exclusively on automated validation for AI-generated educational material.

Even when a response passes structural checks and produces correct numerical results, conceptual inaccuracies may still mislead learners.

Consequently, I recognized the need for independent factual verification and human oversight, particularly when generating educational explanations involving mathematical or technical concepts.

**Reflection and next steps:**

Week 3 strengthened my understanding of structured generation, schema validation and the distinction between syntactic correctness and educational reliability.

The next stage will focus on refining educational content, introducing mathematical verification mechanisms and preparing the system for automatic quiz generation.

These improvements will support ConceptForge's longer-term objective of producing accurate, personalized and adaptive educational resources.

## Future entry milestones
- Entry 1 — by approximately 22 Nov: theory and initial text-generation experiments.
- Entry 2 — by approximately 6 Dec: prompting, structured output and quizzes.
- Entry 3 — by approximately 20 Dec: adaptation, validation and ethics.

The above are planning targets, not official VLE dates.
