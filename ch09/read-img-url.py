from openai import OpenAI


client = OpenAI()

response = client.responses.create(
    model="gpt-5.4",
    input=[
        {
            "type": "message",
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "What's in this image?",
                },
                {
                    "type": "input_image",
                    "detail": "auto",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Beach_at_Fort_Lauderdale.jpg",
                },
            ],
        }
    ],
)


print(response.output_text)