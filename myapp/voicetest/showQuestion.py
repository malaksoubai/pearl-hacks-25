
from openai import OpenAI
from interviewquestions import behavioral_questions as questions
import random

# main.py
import subprocess

randkey = random.randint(1, 10)


print(questions[randkey])