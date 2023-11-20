from gtts import gTTS

translated_audio_dir = 'translated_audio'
os.makedirs(translated_audio_dir, exist_ok=True)
def text_to_speech(translated_text, target_language):
    # Convert translated text to speech using gTTS
    tts = gTTS(text=translated_text, lang=target_language, slow=False)
    return tts

    # Use the generated audio file in your application logic

# Iterate through each translated text file and convert it to speech
for text_file in os.listdir(translated_dir):
    if text_file.endswith(".txt"):
        text_file_path = os.path.join(translated_dir, text_file)
        
        # Read the translated text
        with open(text_file_path, 'r') as file:
            translated_text = file.read()
        
        # Convert the translated text to speech
        target_language = "es"  # Replace with your target language code
        tts = text_to_speech(translated_text, target_language)
        
        # Save the translated text to a new file
        translated_audio_file_path = os.path.join(translated_audio_dir, os.path.splitext(text_file)[0] + f'.mp3')
        tts.save(translated_audio_file_path)
        print(f"Converted {text_file} to {translated_audio_file_path}")
