# Video-to-Text Translation Application

This project is a **Flask-based web application** that extracts speech from videos, converts it to text, and translates it into a target language.

## Features
- Upload a video file
- Extract audio and transcribe speech
- Translate the transcription into the desired language
- Download the transcribed and translated text files

## Technologies Used
- **Flask** (Backend Framework)
- **MoviePy** (Video Processing)
- **SpeechRecognition** (Google Speech API)
- **Deep Translator** (Translation API)
- **pydub** (Audio Processing)
- **HTML, CSS, JavaScript** (Frontend)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/video-translation.git
   cd video-translation
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```sh
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Upload a video file.
2. Select the **source language** of the speech in the video.
3. Select the **target language** for translation.
4. Click on the **Translate** button (a loading animation will appear).
5. View the **recognized text** and its **translation**.
6. Download the text files if needed.

## Troubleshooting
- If `MoviePy` is missing, install it manually:
  ```sh
  pip install moviepy
  ```
- Ensure **ffmpeg** is installed and added to the system path.
- If audio is not being processed, try increasing the `segment_duration` in the code.

## License
This project is open-source under the **MIT License**.

## Author
**Nilesh Wani**

