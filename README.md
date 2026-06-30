# 🧠 SocialSync AI

> **Real-time social cue decoder for autism, elderly & social anxiety support.**  
> Powered by Google Gemini 2.5 Flash · Built for the Kaggle AI Agents Intensive Capstone

---

## 🌟 What is SocialSync AI?

SocialSync AI is a multi-agent AI system that helps people with **autism**, **social anxiety**, and **elderly users** understand the hidden meaning behind everyday conversations.

When someone says *"Great job, really"* — are they being genuine or sarcastic? When a friend says *"I'll be there"* — do they mean it? SocialSync AI decodes these social cues in real time and tells you exactly what to say back.

---

## 🎯 Problem Statement

Over **1 in 36 children** are diagnosed with autism in the US alone. Millions more struggle with social anxiety or age-related communication challenges. These individuals often find it difficult to:

- Detect sarcasm, passive-aggression, or hidden refusals
- Understand the emotional tone behind words
- Know how to respond appropriately in social situations

SocialSync AI bridges this gap using the power of AI agents.

---

## 🤖 The 5-Agent Pipeline

SocialSync AI uses a multi-agent architecture where each agent has a specific role:

| Agent | Role | Technology |
|-------|------|------------|
| 🎙️ **Transcript Agent** | Converts voice recordings to text | Gemini Audio API |
| 📋 **Context Agent** | Analyzes speaker relationship & risk | Rule-based Python |
| 🧠 **Cue Agent** | Detects social cues (sarcasm, hidden refusal, etc.) | Gemini 2.5 Flash |
| 💡 **Coach Agent** | Generates natural response suggestions | Gemini 2.5 Flash |
| 🔗 **Orchestrator** | Coordinates all agents via FastAPI | Python FastAPI |

---

## ✨ Features

- 🎙️ **Voice recording** — Record conversations directly in the browser
- 💬 **Text input** — Type what was said for instant analysis
- 🔍 **Social cue detection** — Genuine, sarcasm, hidden refusal, passive-aggressive, concern, excitement
- 💡 **Response coaching** — What to say + body language tips
- 👴 **Elderly mode** — Simpler, larger explanations
- 🌙 **Light/Dark/System theme** — Accessible for all users
- ⚡ **Real-time analysis** — Results in seconds

---

## 🏗️ Architecture

```
socialsync-ai/
├── backend/                    # Python FastAPI
│   ├── main.py                 # API orchestrator
│   └── agents/
│       ├── context_agent.py    # Relationship context
│       ├── cue_agent.py        # Social cue detection (Gemini)
│       ├── coach_agent.py      # Response coaching (Gemini)
│       └── transcript_agent.py # Audio transcription (Gemini)
└── frontend/                   # Next.js + Tailwind CSS
└── app/
└── page.tsx                    # Main UI
```
---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.10+
- Node.js 18+
- Google Gemini API key (free at [aistudio.google.com](https://aistudio.google.com))

### Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn google-generativeai python-dotenv python-multipart
```

Create a `.env` file in the `backend/` folder:
Start the backend:
```bash
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

---

## 🎬 How to Use

1. Select **who is speaking** (boss, friend, parent, etc.)
2. Either **type** what they said or click **🎙️ Record** to capture audio
3. Click **Analyze with Gemini**
4. See the detected social cue, what they actually meant, and what to say back
5. Enable **Elderly mode** for simpler explanations

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 16, Tailwind CSS, TypeScript |
| Backend | Python FastAPI, Uvicorn |
| AI | Google Gemini 2.5 Flash |
| Audio | Web MediaRecorder API + Gemini Audio |
| Themes | next-themes |

---

## 🏆 Hackathon Track

**Agents for Good** — SocialSync AI helps solve a real human problem: social communication challenges faced by people with autism, social anxiety, and elderly users.

---

## ⚠️ Important Notes

- Never commit your `.env` file or API keys
- The Gemini free tier allows ~20 requests/day — sufficient for demos
- Audio recording requires microphone permission in the browser

---

## 👩‍💻 Built By

**Aalya Gupta**
B.Tech CSE @ Manipal University Jaipur
BS-MS in AI & Cybersecurity @ IIT Patna  
GitHub: [@aalya-gupta05](https://github.com/aalya-gupta05)

---

*Built for the Kaggle AI Agents Intensive Vibe Coding Capstone Project, 2026*