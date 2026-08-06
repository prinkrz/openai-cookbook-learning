from openai import OpenAI
import base64

client = OpenAI()


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = "robot-in-park.png"
base64_image = encode_image(image_path)

response = client.responses.create(
    model="gpt-5.4",
    input=[
        {
            "type": "message",
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Is this image AI generated?"},
                {
                    "type": "input_image",
                    "detail": "auto",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                }
            ]
        }
    ],
)

print(response.output_text)