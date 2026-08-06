from openai import OpenAI

client = OpenAI()

def create_file(file_path):
    with open(file_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="vision"
        )
        return result.id


file_id = create_file("robot-in-park.png")

response = client.responses.create(
    model="gpt-5.4",
    input=[
        {
            "type": "message",
            "role": "user",
            "content": [
                {
                    "type": "input_text",  "text": "what's in this image?"
                },
                {
                    "type": "input_image",
                    "detail": "auto",
                    "file_id": file_id,
                }
            ]
        }
    ]
)

print(response.output_text)