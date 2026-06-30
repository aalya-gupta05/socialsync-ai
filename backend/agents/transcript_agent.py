import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class TranscriptAgent:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def transcribe(self, audio_path: str) -> str:
        try:
            print("===== TRANSCRIPTION DEBUG =====")
            print("Audio path:", audio_path)
            print("File exists:", os.path.exists(audio_path))

            if os.path.exists(audio_path):
                print("File size:", os.path.getsize(audio_path), "bytes")

            audio_file = genai.upload_file(path=audio_path)
            print("✅ Upload successful")

            response = self.model.generate_content([
                audio_file,
                "Transcribe exactly what is said in this audio. Respond with ONLY the transcribed text."
            ])

            print("✅ Gemini Response:", response.text)

            return response.text.strip()

        except Exception as e:
            print("❌ ERROR:", repr(e))
            raise
