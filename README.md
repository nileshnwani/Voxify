# Voxify - Recognizer and Translator

Voxify is a Flask-based web application that extracts audio from videos, transcribes the speech into text, and translates it into a specified language.

## Features
- Extracts audio from uploaded video files.
- Splits long audio files into 2-minute segments.
- Transcribes speech using Google Speech Recognition.
- Translates transcriptions into the desired language using Deep Translator.
- Provides downloadable text files for transcriptions and translations.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd Voxify-Recognizer-Translator
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```sh
   python app.py
   ```

2. Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. Upload a video file, select the source and target language, and click "Translate".

4. View the transcription and translation results.

## Requirements
Ensure you have `ffmpeg` installed for audio processing. Install it using:
```sh
sudo apt install ffmpeg  # For Linux
brew install ffmpeg      # For macOS
choco install ffmpeg     # For Windows
```

## Dependencies
- Flask
- moviepy
- speechrecognition
- deep-translator
- pydub

## License
This project is licensed under the MIT License.


## Author
**Nilesh Wani**

