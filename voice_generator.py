import os
import requests
from config import CHARACTER_VOICE_MAP, VOICES_DIR

def tts_hf_suno(character, text, filename):
    """
    Generate speech using Hugging Face Suno TTS Space.
    Args:
        character (str): Character name (used for speaker selection if needed)
        text (str): Text to be synthesized
        filename (str): Output WAV file name
    """
    speaker = "female" if character.lower() not in ["narrator", "male"] else "male"
    url = "https://suno-tts.hf.space/run/predict"
    payload = {"data": [text, speaker]}
    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        audio_url = response.json()["data"][0]
        audio = requests.get(audio_url)
        out_path = os.path.join(VOICES_DIR, filename)
        with open(out_path, "wb") as f:
            f.write(audio.content)
        print(f"Generated voice for {character}: {filename}")
    except Exception as e:
        print(f"Error generating voice for {character}: {e}")

def parse_script(script_path):
    # Expects lines like "CHARACTER: dialogue"
    lines = []
    with open(script_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if ":" in line:
                character, dialogue = line.split(":", 1)
                lines.append((character.strip(), dialogue.strip(), idx))
    return lines

if __name__ == "__main__":
    os.makedirs(VOICES_DIR, exist_ok=True)
    script_lines = parse_script("script.txt")
    for character, dialogue, idx in script_lines:
        filename = f"{character.lower()}_line{idx+1}.wav"
        tts_hf_suno(character, dialogue, filename)