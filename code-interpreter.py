from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
    tools=[{
        "type": "code_interpreter",
        "container": {"type": "auto"}
    }],
    input="Solve this equation: 3x + 2 = 14"
)

print(response.output_text)