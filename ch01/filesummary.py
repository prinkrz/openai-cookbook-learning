from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Analyze the pdf and provide a summary of the key points"
                },
                {
                    "type": "input_file",
                    "file_url": "https://www.bseindia.com/xml-data/corpfiling/AttachHis/e76d0ca2-740a-4e0f-986a-2ad0ad39d515.pdf"
                }
            ]
        }
    ]
)

print(response.output_text)