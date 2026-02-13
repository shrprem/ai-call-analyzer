import subprocess
import os
from transcribe import transcribe_audio


def analyze_with_ollama(transcript: str) -> str:
    """
    Sends transcript to Ollama llama3 for analysis.
    """

    prompt = f"""
You are an expert call analyst.

Analyze this call transcript and provide:

1. Emotional tone
2. Power dynamics
3. Trust level
4. Risk signals

Transcript:
{transcript}
"""

    print("🧠 Sending transcript to Ollama...")

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8"
    )

    return result.stdout


if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(current_dir, "sample.wav")

    print("🎧 Starting Call Analysis...\n")

    transcript = transcribe_audio(audio_path)

    print("\n📄 Transcript Ready\n")

    analysis = analyze_with_ollama(transcript)

    print("\n--- AI CALL ANALYSIS ---\n")
    print(analysis)
