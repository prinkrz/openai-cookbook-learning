from openai import OpenAI

client = OpenAI()

with open("prompt.txt", "r", encoding="utf-8") as f:
    instructions = f.read()

response = client.responses.create(
    model="gpt-5.4-mini",
    instructions=instructions,
    input="How would I declare a variable for  a last name?"
)

print(response.output_text)