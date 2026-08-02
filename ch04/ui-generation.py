from enum import Enum
from typing import List

from openai import OpenAI
from pydantic import BaseModel

import json

client = OpenAI()

class UIType(str, Enum):
    div = "div"
    button = "button"
    header = "header"
    section = "section"
    field = "field"
    form ="form"

class Attribute(BaseModel):
    name: str
    value: str

class UI(BaseModel):
    type: UIType
    label: str
    children: List["UI"]
    attributes: List[Attribute]

UI.model_rebuild()

class Response(BaseModel):
    ui: UI

response = client.responses.parse(
    model="gpt-5.4-mini",
    input=[
        {
            "role": "system",
            "content": "You are a UI generator AI. Convert the user input into a UI."
        },
        {
            "role": "user",
            "content": "Make a User profile form"
        },
    ],
    text_format=Response
)

ui = response.output_parsed

print(ui)