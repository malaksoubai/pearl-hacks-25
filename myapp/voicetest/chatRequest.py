import json
from openai import OpenAI
from interviewquestions import behavioral_questions as questions
import random

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("DEEPSEEK-KEY")

print(f"Your API Key: {api_key}")  # For testing purposes (Remove in production)


from showQuestion import randkey

# # main.py
# import subprocess



# command = ['whisper', 'output.mp3', '--model', 'base']

# # Run the command using subprocess
# try:
#     result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     # print(f"Output: {result.stdout}")
#     # print(f"Error: {result.stderr}")
# except subprocess.CalledProcessError as e:
#     print(f"Error occurred while running the command: {e}")


#ALREADY RUNNING THIS PROCESS IN APP ROUTE, separate button
# if __name__ == "__main__":
#     subprocess.run(['python', 'recording.py'])  # This runs recording.py as a standalone script

# command = ['whisper', 'output.mp3', '--model', 'base']

# # Run the command using subprocess
# try:
#     result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     print(f"Output: {result.stdout}")
#     print(f"Error: {result.stderr}")
# except subprocess.CalledProcessError as e:
#     print(f"Error occurred while running the command: {e}")










# with open('output.txt', 'r') as file:
#     output_txt = file.read()


# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="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",
# )

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
#       "content": f"based on this question: {questions[randkey]}, evaluate the quality of {output_txt}. Include output of the original question and response in your answer."
#     }
#   ]
# )
# print(completion.choices[0].message.content)

# # # Prepare the response
# # response_data = {
# #     "question": questions[randkey],
# #     "python_output": output_txt,
# #     "evaluation": completion.choices[0].message.content
# # }

# # # Return the result as a JSON object
# # print(json.dumps(response_data))