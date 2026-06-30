import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class CoachAgent:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, text: str, cue: dict, speaker_role: str, is_elderly: bool = False) -> dict:

        elderly_note = "The user is elderly so use very simple, short words they can easily understand." if is_elderly else ""

        prompt = f"""You are SocialSync AI — a compassionate social coach helping people with autism, social anxiety, or elderly users respond to conversations naturally.

WHAT WAS SAID: "{text}"
SPEAKER ROLE: {speaker_role}
DETECTED CUE: {cue['cue_type']}
ACTUAL MEANING: {cue['actual_meaning']}
TONE: {cue['tone']}
{elderly_note}

Your job is to help the user respond appropriately to this exact situation.

CRITICAL RULES:
- Suggest a response that directly addresses what was said
- Match the relationship (e.g. casual with friend, respectful with boss)
- Keep suggested response short and natural (1-2 sentences max)
- Be specific to the actual words said, not generic

Respond ONLY with valid JSON, no markdown:
{{
  "suggested_response": "what the user should say out loud",
  "body_language": "specific body language tip for this situation",
  "urgency": "immediate, normal, or relaxed",
  "why_this_works": "brief reason why this response works",
  "elderly_tip": "simple one sentence tip" or null,
  "color_code": "red, orange, yellow, or green based on social risk"
}}"""

        response = self.model.generate_content(prompt)
        raw = response.text.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()

        try:
            result = json.loads(raw)
        except:
            result = {
                "suggested_response": "Could you say that again?",
                "body_language": "Maintain eye contact and stay calm.",
                "urgency": "normal",
                "why_this_works": "Buying time to process.",
                "elderly_tip": None,
                "color_code": "green"
            }

        return result