
# main.py
import subprocess


command = ['whisper', 'output.mp3', '--model', 'base']

# Run the command using subprocess
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Output: {result.stdout}")
    print(f"Error: {result.stderr}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while running the command: {e}")