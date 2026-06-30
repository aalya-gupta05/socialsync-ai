from fastapi import FastAPI, File, UploadFile
import shutil
import os as os_module
from agents.transcript_agent import TranscriptAgent
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.cue_agent import CueAgent
from agents.coach_agent import CoachAgent
from agents.context_agent import ContextAgent
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="SocialSync AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cue_agent = CueAgent()
coach_agent = CoachAgent()
context_agent = ContextAgent()
transcript_agent = TranscriptAgent()

class AnalyzeRequest(BaseModel):
    text: str
    speaker_role: str = "friend"
    is_elderly: bool = False

@app.get("/")
def root():
    return {"status": "SocialSync AI is running!"}

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    context = context_agent.analyze(req.speaker_role)
    cue = cue_agent.detect(req.text, context)
    coach = coach_agent.generate(req.text, cue, req.speaker_role, req.is_elderly)
    
    return {
        "input": req.text,
        "speaker_role": req.speaker_role,
        "context": context,
        "cue": cue,
        "coach": coach
    }
@app.post("/analyze-audio")
async def analyze_audio(
    audio: UploadFile = File(...),
    speaker_role: str = "friend",
    is_elderly: bool = False
):
    # Save uploaded audio temporarily
    temp_path = f"temp_{audio.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    try:
        # Transcribe
        text = transcript_agent.transcribe(temp_path)
    except Exception as e:
        print("TRANSCRIPTION ERROR:", repr(e))
        raise
        
        # Run through the same pipeline
        context = context_agent.analyze(speaker_role)
        cue = cue_agent.detect(text, context)
        coach = coach_agent.generate(text, cue, speaker_role, is_elderly)

        return {
            "input": text,
            "speaker_role": speaker_role,
            "context": context,
            "cue": cue,
            "coach": coach
        }
    finally:
        if os_module.path.exists(temp_path):
            os_module.remove(temp_path)    
