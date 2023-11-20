import nltk

nltk.download('punkt')

from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    #slice all text on the basis of sentences and translate each sentence
    text = nltk.sent_tokenize(text)
    translation = ""
    for i in text:
        translation = translation + translator.translate(i, dest=target_language).text + "."
    return translation

translated_dir = 'translated'
os.makedirs(translated_dir, exist_ok=True)
# Iterate through each transcribed text file and translate it
for text_file in os.listdir(audio_dir):
    if text_file.endswith(".txt"):
        text_file_path = os.path.join(audio_dir, text_file)
        
        # Read the transcribed text
        with open(text_file_path, 'r') as file:
            original_text = file.read()
        
        # Translate the text to the desired language
        target_language = "es"  # Replace with your target language code
        translated_text = translate_text(original_text, target_language)
        
        # Save the translated text to a new file
        translated_text_file_path = os.path.join(translated_dir, os.path.splitext(text_file)[0] + f'.txt')
        with open(translated_text_file_path, 'w') as translated_text_file:
            translated_text_file.write(translated_text)
        print(f"Translated {text_file} to {translated_text_file_path}")
