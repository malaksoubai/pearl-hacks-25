import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
from pydub import AudioSegment
import subprocess


def record_audio(filename="output.wav", duration=10, samplerate=44100):
    """Records audio from the microphone and saves it as a WAV file."""
    print("Recording...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    print("Finished recording.")
    write(filename, samplerate, recording)
    return filename



def convert_to_mp3(wav_filename, mp3_filename="output.mp3"):
  """Converts a WAV file to MP3 format."""
  audio = AudioSegment.from_wav(wav_filename)
  audio.export(mp3_filename, format="mp3")
  print(f"File converted to {mp3_filename}")
  os.remove(wav_filename)
  return mp3_filename

if __name__ == "__main__":
    wav_filename = record_audio()
    mp3_file = convert_to_mp3(wav_filename)
    path = os.path.dirname(mp3_file) 
    print(path)

output_file = 'output.txt'

command = ['whisper', 'output.mp3', '--model', 'base']


with open(output_file, 'w') as f:
    # Run the command and redirect stdout to the file
    try:
        result = subprocess.run(command, check=True, stdout=f, stderr=subprocess.PIPE, text=True)
        print(f"Transcription saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the command: {e}")

# # Run the command using subprocess
# try:
#     result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     print(f"Output: {result.stdout}")
#     print(f"Error: {result.stderr}")
# except subprocess.CalledProcessError as e:
#     print(f"Error occurred while running the command: {e}")
