# Foreign Whispers - Video Translation

Foreign Whispers is a comprehensive video translation system that takes a YouTube video as input, extracts the audio, transcribes the speech, translates the text to a target language, and generates the translated audio.

## Features

- Download YouTube videos and associated closed captions (subtitles)
- Transcribe the audio using the Whisper speech recognition model
- Translate the transcribed text to a target language using the Google Translate API
- Convert the translated text to speech using the Google Text-to-Speech (gTTS) library
- Modular and extensible design for easy maintenance and future expansion

## Getting Started

### Prerequisites

- Python 3.6 or higher
- The following Python libraries:
  - `pytube`
  - `whisper`
  - `googletrans`
  - `gtts`
  - `subprocess`
  - `os`
  - `moviepy`

### Usage

1. Open the `project.ipynb` Jupyter Notebook file.
2. Run the cells in the notebook to execute the different milestones of the project.
3. Customize the code as needed, such as adding more video URLs or changing the target language.

## Milestones

1. **Source Videos and Closed Captions**: Download YouTube videos and associated closed captions.
2. **Speech to Text**: Transcribe the audio from the downloaded videos using the Whisper speech recognition model.
3. **Source Text to Target Text**: Translate the transcribed text to a target language using the Google Translate API.
4. **Target Text to Speech**: Convert the translated text to speech using the Google Text-to-Speech (gTTS) library.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
