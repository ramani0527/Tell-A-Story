from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
SYSTEM_PROMPT =("You are a masterful collaborative storyteller."
                "You will write a story one part at a time, building on the previous parts."
                "You will maintain consistency in the story's plot, setting, "
                "character personalities, and world rules."
                "Never contradict earlier parts of the story."
                "You can only write the next part of the story, never rewrite or edit previous parts"
                "Always end your part of the story with a cliffhanger or an intriguing question to keep the reader hooked"
                "Write in vivid but concise third-person narrative. Keep the tone engaging and fun.")

def build_continue_prompt(story, genre, rules):
    return f"""
You are writing a {genre} story.
Follow these rules: {", ".join(rules)}.

Story so far:
{story}

Continue the story with 1–2 coherent paragraphs.
"""


def build_choices_prompt(story, genre, rules):
    return f"""
You are writing a {genre} story.
Follow these rules: {", ".join(rules)}.

Story so far:
{story}

Give 3 branching options for what happens next.
Each option should be 1–2 sentences.
"""


def call_llm(prompt, temperature):
    # TODO: Replace with your actual LLM call
    # Example (OpenAI):
    #
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=temperature
    # )
    # return response.choices[0].message.content.strip()
    #
    return "LLM response placeholder"

from fastapi import FastAPI
from pydantic import BaseModel
from story_engine import call_llm

app = FastAPI()

class StartRequest(BaseModel):
    title: str
    genre: str
    initial_hook: str
    temperature: float

@app.post("/start")
def start_story(req: StartRequest):
    prompt = f"""
Write a strong opening paragraph (150–250 words) for a story titled "{req.title}".
Genre: {req.genre}

Use the following hook or setting as inspiration:
{req.initial_hook}

The paragraph should be immersive, descriptive, and set the tone for the story.
"""

    opening = call_llm(prompt, req.temperature)

    return {"opening_paragraph": opening.strip()}
