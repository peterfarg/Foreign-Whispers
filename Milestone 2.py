import os
import subprocess
import whisper

model = whisper.load_model("base")  # You can choose different models like "small", "medium", "large", or "base".

def extract_audio(video_path, audio_output_path):
    command = f"ffmpeg -i \"{video_path}\" -ab 160k -ac 2 -ar 44100 -vn \"{audio_output_path}\""
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output.decode('utf-8')}")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

video_dir = 'videos'
audio_dir = 'audio'
os.makedirs(audio_dir, exist_ok=True)

for video_file in os.listdir(video_dir):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(video_dir, video_file)
        audio_output_path = os.path.join(audio_dir, os.path.splitext(video_file)[0] + '.mp3')
        extract_audio(video_path, audio_output_path)
        text = transcribe_audio(audio_output_path)
        text_file_path = os.path.join(audio_dir, os.path.splitext(video_file)[0] + '.txt')
        with open(text_file_path, 'w') as text_file:
            text_file.write(text)
        print(f"Transcribed audio from {video_file} to {text_file_path}")
