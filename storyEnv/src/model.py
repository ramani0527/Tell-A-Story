# llm.py
from pydantic import BaseModel
from typing import List

class StoryRequest(BaseModel):
    story: str
    user_input: str = ""
    temperature: float
    genre: str
    rules: List[str]
