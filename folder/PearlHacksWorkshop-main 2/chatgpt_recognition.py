from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

# Load your API key and set up ChatGPT client
load_dotenv()
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# Read an image as a stream of bytes
with open("folder/PearlHacksWorkshop-main 2/cat.jpg", "rb") as f:
    image = f.read()

# Encode the image as a base64 string
b64 = base64.b64encode(image).decode('utf-8')

# Send the query
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                # Replace this prompt for more specific use cases
                {"type": "text", "text": """What is in this picture?"""},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{b64}"
                    }
                },
            ],
        }
    ],
    max_tokens=300
)

print(completion.choices[0].message.content)