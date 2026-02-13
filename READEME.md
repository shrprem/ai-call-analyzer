# AI Call Analyzer

An AI-powered call analysis system that transcribes audio conversations and generates psychological and conversational insights using local Large Language Models. The project runs fully offline using Whisper for speech recognition and Ollama for AI inference.

---

## Problem Statement

Many sales, support, and business calls contain important emotional and contextual signals that are difficult to analyze manually. Traditional call review processes are time-consuming and subjective.

This project solves that problem by:

- Automatically converting spoken conversations into structured text
- Identifying emotional tone and conversational intent
- Providing AI-driven insights into trust level, risk signals, and communication dynamics
- Allowing users to analyze calls locally without relying on cloud APIs or sharing sensitive data

The goal is to help users quickly understand the purpose and sentiment of conversations through AI-assisted analysis.

---

## Features

- Speech-to-text transcription using OpenAI Whisper
- Emotional tone and intent analysis using local LLMs via Ollama
- Offline AI processing with no external API dependency
- Streamlit web interface for uploading and analyzing audio files
- Multilingual support including English and Hindi audio

---

## How It Works

1. Upload a call recording (.wav, .mp3, .m4a)
2. Whisper converts speech into text
3. Ollama runs a local language model to analyze the transcript
4. The system generates structured call insights

---

## Tech Stack

- Python
- Streamlit
- Whisper Speech Recognition
- Ollama Local LLM Runtime
- Llama3 / Phi3 Models

---

## Project Structure

-app.py # Streamlit UI
-analyze_call.py # AI analysis logic
-transcribe.py # Whisper transcription
-prompts.py # Prompt templates for analysis


---

## Installation (Local Setup)

Clone the repository:

-git clone https://github.com/shrprem/ai-call-analyzer.git
-cd ai-call-analyzer


Create a virtual environment:
-python -m venv venv

Activate the environment:
-venv\Scripts\activate


Install dependencies:
-pip install -r requirements.txt


Install Ollama and download a model:
-ollama pull phi3

Run the application:
-streamlit run app.py


---

## Future Improvements

- Real-time call assistant mode
- Emotion timeline visualization
- Live conversational suggestions
- Cloud demo deployment version

---

## Author

Prem  
AI and Software Development Student


