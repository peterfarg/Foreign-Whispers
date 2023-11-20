import streamlit as st
from googletrans import Translator
import nltk
from gtts import gTTS
import subprocess
import whisper
import os
from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip

model = None
print("loading model: base")
async def load_model():
    model = await whisper.load_model("base")  # You can choose different models like "small", "medium", "large", or "base".
    print("Loaded model: base")

load_model()

video_dir = 'videos'
audio_dir = 'audio'
translated_video_dir = 'translated_videos'
translated_audio_dir = 'translated_audio'

def main():
    st.title("Foreign Whispers - Video Translation")

    # Form for user input
    video_url = st.text_input("Enter YouTube video URL:")
    target_language = st.selectbox("Select Target Language:", ["es", "fr","en","zh","ur"])  # Add more options as needed
    video_title = ""
    if st.button("Translate and Generate Subtitles"):
        # Your logic for video translation here
        try:
            # Create a YouTube object with the URL.
            yt = YouTube(video_url)
            
            # Download the best quality video
            video_stream = yt.streams.get_highest_resolution()
            if video_stream:
                video_stream.download(output_path='videos/')
                print(f'Downloaded video: {yt.title}.mp4')
                video_title = yt.title
            # Download the English captions (subtitles)
            en_caption = yt.captions.get_by_language_code('en')
            if en_caption:
                en_caption_srt = en_caption.generate_srt_captions()
                with open(f'videos/{yt.title}.srt', 'w') as file:
                    file.write(en_caption_srt)
                    print(f'Downloaded caption: {yt.title}.srt')
        except Exception as e:
            print(f'Failed to download {video_url}: {str(e)}')

        # Extract audio from the video
        #get the video path
        video_path = os.path.join(video_dir, video_title + ".mp4")
        audio_path = os.path.join(audio_dir, video_title + ".mp3")
        text_file_path = os.path.join(audio_dir, video_title + '.txt')
        if video_path.endswith(".mp4"):
            print(f"Processing {video_path}")
            
            # Extract the audio from the video
            extract_audio(video_path, audio_path)
            
            # Transcribe the audio to text
            text = transcribe_audio(audio_path)
            
            # Save the transcription to a file
            text_file_path = os.path.join(audio_dir, os.path.splitext(text_file_path) + '.txt')
            with open(text_file_path, 'w') as text_file:
                text_file.write(text)
            print(f"Transcribed audio from {video_path} to {text_file_path}")


        # Translate the text
        translated_text = translate_text(text, target_language)
         # Convert translated text to speech
        tt = text_to_speech(translated_text)
        translated_audio_path = os.path.join(translated_audio_dir, video_title + ".mp3")
        tt.save(translated_audio_path)
        print(f"Translated text to speech and saved to {translated_audio_path}")

        # Display translated text
        st.subheader("Translated Text:")
        st.write(translated_text)

       

        # Display the translated video (if applicable)
        st.subheader("Translated Video:")
        #embed audio to the ui
        st.audio(translated_audio_path)
        # Add logic to embed or link the translated video if available

def translate_and_generate_subtitles(video_url, target_language):
    # Implement translation logic using googletrans
    # This is a placeholder, replace it with your actual implementation
    #download video from youtube

    translator = Translator()
    translated_text = translator.translate(original_text, dest=target_language).text

    # Use translated_text in your application logic
    return translated_text


def translate_text(text, target_language):
    translator = Translator()
    #slice all text on the basis of sentences and translate each sentence
    text = nltk.sent_tokenize(text)
    translation = ""
    for i in text:
        translation = translation + translator.translate(i, dest=target_language).text + "."
    return translation

def text_to_speech(translated_text, target_language):
    # Convert translated text to speech using gTTS
    tts = gTTS(text=translated_text, lang=target_language, slow=False)
    return tts


def extract_audio(video_path, audio_output_path):
    # Command to extract audio using ffmpeg
    command = f"ffmpeg -i \"{video_path}\" -ab 160k -ac 2 -ar 44100 -vn \"{audio_output_path}\""
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.output.decode('utf-8')}")

def transcribe_audio(audio_path):
    # Load audio and run the Whisper model to transcribe it
    result = model.transcribe(audio_path)
    return result['text']

# Directory where the videos are saved


# def text_to_speech(translated_text):
#     # Convert translated text to speech using pyttsx3
#     engine = pyttsx3.init()
#     engine.say(translated_text)
#     engine.runAndWait()


def download_video(url):
    # Download the video and the captions
    try:
        # Create a YouTube object with the URL.
        yt = YouTube(url)
        
        # Download the best quality video
        video_stream = yt.streams.get_highest_resolution()
        if video_stream:
            video_stream.download(output_path='videos/')
            print(f'Downloaded video: {yt.title}.mp4')
        
        # Download the English captions (subtitles)
        en_caption = yt.captions.get_by_language_code('en')
        if en_caption:
            en_caption_srt = en_caption.generate_srt_captions()
            with open(f'videos/{yt.title}.srt', 'w') as file:
                file.write(en_caption_srt)
                print(f'Downloaded caption: {yt.title}.srt')
    except Exception as e:
        print(f'Failed to download {url}: {str(e)}')
if __name__ == "__main__":
    main()
