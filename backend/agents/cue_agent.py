import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class CueAgent:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def detect(self, text: str, context: dict) -> dict:
        
        prompt = f"""You are a social cue detection AI helping people with autism, social anxiety, or elderly users understand conversations.

Analyze this statement and detect the social cue:

TEXT: "{text}"
SPEAKER ROLE: {context['speaker_role']}
RELATIONSHIP: {context['description']}
FORMALITY: {context['formality']}
SARCASM RISK: {context['sarcasm_risk']}

Classify the social cue as ONE of:
- genuine: sincere, positive, straightforward
- sarcasm: words mean the opposite of what's said
- hidden_refusal: saying yes but meaning no
- passive_aggressive: indirect expression of frustration
- concern: genuine worry or care
- excitement: genuine enthusiasm
- confusion: unclear or ambiguous meaning

Respond ONLY with valid JSON, no markdown:
{{
  "cue_type": "one of the above",
  "confidence": 0.0 to 1.0,
  "explanation": "brief explanation of why",
  "tone": "the emotional tone detected",
  "literal_meaning": "what they literally said",
  "actual_meaning": "what they actually mean"
}}"""

        response = self.model.generate_content(prompt)
        raw = response.text.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        
        try:
            result = json.loads(raw)
        except:
            result = {
                "cue_type": "genuine",
                "confidence": 0.5,
                "explanation": "Could not analyze",
                "tone": "neutral",
                "literal_meaning": text,
                "actual_meaning": text
            }
        
        return result