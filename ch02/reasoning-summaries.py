from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4",
    input="What is the capital of France?",
    reasoning={"effort": "low", "summary": "auto"},
)

print(response.output)