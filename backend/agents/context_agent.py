class ContextAgent:
    
    def __init__(self):
        self.relationship_db = {
            "boss": {
                "power_dynamic": "high",
                "formality": "formal",
                "sarcasm_risk": 0.35,
                "description": "Workplace superior"
            },
            "friend": {
                "power_dynamic": "equal",
                "formality": "casual",
                "sarcasm_risk": 0.50,
                "description": "Close friend"
            },
            "colleague": {
                "power_dynamic": "equal",
                "formality": "semi-formal",
                "sarcasm_risk": 0.25,
                "description": "Work peer"
            },
            "parent": {
                "power_dynamic": "high",
                "formality": "semi-formal",
                "sarcasm_risk": 0.20,
                "description": "Family elder"
            },
            "teacher": {
                "power_dynamic": "high",
                "formality": "formal",
                "sarcasm_risk": 0.15,
                "description": "Educator"
            },
            "stranger": {
                "power_dynamic": "unknown",
                "formality": "formal",
                "sarcasm_risk": 0.10,
                "description": "Unknown person"
            }
        }

    def analyze(self, speaker_role: str) -> dict:
        role = self.relationship_db.get(
            speaker_role.lower(),
            self.relationship_db["stranger"]
        )
        return {
            "speaker_role": speaker_role,
            "power_dynamic": role["power_dynamic"],
            "formality": role["formality"],
            "sarcasm_risk": role["sarcasm_risk"],
            "description": role["description"]
        }