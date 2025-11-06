SUMMARY = """Create a detailed, long form summary for the following document. The summary should be in the same language as the document itself. Do not mention the document itself. Do not mention that it is a summary explicitly, no need for a header or title. Respond in markdown format.
Document:
{document}"""

QA = """Create a list of 10 question-answer pairs for the following document. The questions and answers should be in the same language as the document itself. Do not mention the document itself, the questions should be self-contained. Do not mention that it is a QA explicitly, no need for a header or title. Only respond with the qa-pairs. Respond in markdown format like this:
- Question:
- Answer:

- Question:
- Answer:

...

Use language appropriate replacements for "Question:" and "Answer:", e.g., "Frage:" and "Antwort:" if the document is in German.
Document:
{document}"""

EDU_MATERIAL = """Transform the following document into educational learning material. The learning material should be in the same language as the document itself. Do not refer to the document itself in the learning material, it should be self-contained. Do not mention that it is an educational material explicitly. Respond with the created material in markdown.
Document:
{document}"""

EXAMS = """I want to test whether my students have read the following document. Create 5 different exams to test this. The exams should have different styles, so I can pick the one I like best. The exam must contain diverse tasks. Also include the solution for each task to help me grade the exams later on. The exam must be in the same language as the document itself. Do not mention the document itself. The students already know what this exam is about. Try to make the questions as hard as possible, but self-contained to the document. Each exam must include 5 easy, 5 medium, and 5 hard tasks. Respond in markdown format.
Document:
{document}"""

ACTIVE_READING = """Interleave the following document with active reading elements. The elements should be in the same language as the document itself.
Here's a typical active reading workflow that helps with comprehension and retention:
# Active Reading Workflow
## Before Reading
Preview the material - Skim headings, subheadings, intro/conclusion, bold terms, and visuals to get the big picture
Set a purpose - Ask yourself why you're reading this and what you want to get out of it
Activate prior knowledge - Think about what you already know about the topic

##During Reading
Annotate as you go - Underline key points, circle unfamiliar terms, write margin notes with reactions or questions
Ask questions - Turn headings into questions, note confusing parts, wonder about implications
Visualize and connect - Create mental images, relate new info to what you know, look for patterns
Pause periodically - Stop at natural breaks to summarize what you just read in your own words
Monitor comprehension - Notice when you lose focus or understanding, then reread or slow down

##After Reading
Summarize main ideas - Write a brief summary without looking back at the text
Review your annotations - Look over your notes and highlights
Make connections - Think about how this relates to other reading or your own experience
Generate questions - What are you still wondering about? What would you ask the author?
Reflect on application - How might you use this information?


The key is engagement—actively thinking about and responding to the text rather than passively letting words pass by. 
Respond in markdown format like this:


The interleaved document should simulate the process of someone actively reading the document, including the before reading, during reading, and after reading steps. It should also include the persons thinking process.
Document:
{document}"""


PROMPTS = {
    "summary": SUMMARY,
    "qa": QA,
    "edu_material": EDU_MATERIAL,
    "exams": EXAMS,
    "active_reading": ACTIVE_READING
}