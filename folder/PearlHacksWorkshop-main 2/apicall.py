# from openai import OpenAI
# import base64

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="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",
# )

# #Read image
# with open("folder/PearlHacksWorkshop-main 2/cat.jpg", "rb") as f:
#     image = f.read()

# # Encode the image as a base64 string
# b64 = base64.b64encode(image).decode('utf-8')


# completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },

#   extra_body={},
#   model="deepseek/deepseek-chat:free",

#   messages=[
#     {
#       "role": "user",
#       "content": [
#           # Replace this prompt for more specific use cases
#                 {"type": "text", "text": """What is in this picture?"""},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{b64}"
#                     }
#                 },
#       ]
#     }
#   ],
#     max_tokens=300
# )
# print(completion.choices[0].message.content)

import ollama
import os

screenshots_folder = "screenshots"

screenshot_list = [os.path.join(screenshots_folder, f) for f in os.listdir(screenshots_folder) if os.path.isfile(os.path.join(screenshots_folder, f))]
print(screenshot_list)

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': 'Assess interviewee eye contact and body language and provide improvements in 4 sentences:',
			'images': screenshot_list
		}
	],
)

print(res['message']['content'])