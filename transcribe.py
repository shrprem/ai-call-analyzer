import whisper
import os

def transcribe_audio(audio_path: str) -> str:
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print("🔊 Loading Whisper model...")
    model = whisper.load_model("base")

    print("📝 Transcribing audio...")
    result = model.transcribe(audio_path)

    return result["text"]


if __name__ == "__main__":
    # 👇 THIS PART FIXES WINDOWS PATH ISSUES
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(current_dir, "sample.wav")

    print("📂 Using audio file:", audio_path)

    text = transcribe_audio(audio_path)

    print("\n--- TRANSCRIPT ---")
    print(text)
