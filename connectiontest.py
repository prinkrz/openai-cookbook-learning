from openai import OpenAI


client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write one sentence: phrase of the day"
)

print(response.output_text)