from openai import OpenAI
import base64

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4",
    input="Generate an image of a robot enjoing a sunny day in the park, carrying an umbrella. " \
    "Add a small kid with robot as his friend (boy). Put a sunglass for robot & kid. Add a dog as friend",
    tools= [{
        "type": "image_generation"
    }],
)

# Save the image to a file
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]
    with open("robot4.png", "wb") as f:
        f.write(base64.b64decode(image_base64))