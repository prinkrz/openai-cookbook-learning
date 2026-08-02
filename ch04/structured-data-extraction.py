from openai import OpenAI
from pydantic import BaseModel
import json

client = OpenAI()

class ResearchPaperExtraction(BaseModel):
    title: str
    authors: list[str]
    abstracts: str
    keywords: list[str]

response = client.responses.parse(
    model="gpt-5.4-mini",
    input=[
        {
            "role": "system",
            "content": "You are an expert at structured data extraction. You will be given unstructured text from a research paper and should convert it into the given structure."
        },
        {
            "role": "user",
            "content": (
                "Attention Is All you Need by Ashish Vaswani, Noam Shazeer, "
                "Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, "
                "Łukasz Kaiser, and Illia Polosukhin. We propose the "
                "Transformer, a sequence transduction architecture based "
                "entirely on attention. Keywords: transformers, attention, "
                "sequence transduction."
            ),
        },
    ],
    text_format=ResearchPaperExtraction
)

research_paper = response.output_parsed
print(json.dumps(research_paper.__dict__, indent=4))