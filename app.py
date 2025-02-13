from flask import Flask, render_template, request, send_file
import moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import speech_recognition as sr
from deep_translator import GoogleTranslator
from pydub import AudioSegment

app = Flask(__name__)

def extract_audio(video_path, audio_path):
    """Extracts audio from the video file and saves it as WAV."""
    print(f"Extracting audio from {video_path}...")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    video.close()
    print(f"Audio extracted and saved as {audio_path}")

def recognize_speech(audio_path, source_language):
    """Recognizes speech from an audio file using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as audio_file:
        audio = recognizer.record(audio_file)

        try:
            recognized_text = recognizer.recognize_google(audio, language=source_language)
            return recognized_text
        except sr.UnknownValueError:
            print("⚠️ Speech recognition could not understand the audio.")
            return "Speech recognition could not understand the audio."
        except sr.RequestError:
            print("⚠️ Could not request results from Google Speech Recognition.")
            return "Could not request results from Google Speech Recognition."

def translate_text(text, target_language):
    """Translates text to the target language using Deep Translator."""
    translator = GoogleTranslator(source="auto", target=target_language)
    translated_text = translator.translate(text)
    return translated_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_file = request.files['video']
        source_language = request.form.get('source_language')
        target_language = request.form.get('target_language')

        if video_file and source_language and target_language:
            video_path = "uploaded_video.mp4"
            audio_path = "audio.wav"

            video_file.save(video_path)

            # Extract audio from the video
            extract_audio(video_path, audio_path)

            # Split audio into segments
            audio = AudioSegment.from_wav(audio_path)
            segment_duration = 2 * 60 * 1000  # 2 minutes in milliseconds
            num_segments = len(audio) // segment_duration + 1

            combined_recognized = []
            combined_translation = []

            print(f"🔄 Processing {num_segments} segments...")

            for segment_index in range(num_segments):
                start_time = segment_index * segment_duration
                end_time = min((segment_index + 1) * segment_duration, len(audio))

                segment_audio = audio[start_time:end_time]
                segment_audio_path = f"segment_{segment_index}.wav"
                segment_audio.export(segment_audio_path, format="wav")

                print(f"🎤 Processing Segment {segment_index + 1}/{num_segments}...")

                recognized_text = recognize_speech(segment_audio_path, source_language)
                translated_text = translate_text(recognized_text, target_language)

                combined_recognized.append(f"Segment {segment_index + 1}:\n{recognized_text}")
                combined_translation.append(f"Segment {segment_index + 1}:\n{translated_text}")

                os.remove(segment_audio_path)  # Clean up segment file

            # Save transcriptions
            recognized_text_path = "recognized.txt"
            translated_text_path = "translated.txt"

            with open(recognized_text_path, "w", encoding="utf-8") as file:
                file.write("\n\n".join(combined_recognized))

            with open(translated_text_path, "w", encoding="utf-8") as file:
                file.write("\n\n".join(combined_translation))

            print("✅ Processing complete. Transcription and translation saved.")

            return render_template('result.html',
                                   recognized_text=combined_recognized,
                                   translated_text=combined_translation)

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
