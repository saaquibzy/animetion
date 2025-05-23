# voice_generator.py

import os
import requests
from config import ELEVENLABS_API_KEY, CHARACTER_VOICE_MAP, VOICES_DIR

def tts_elevenlabs(character, text, filename):
    voice_id = CHARACTER_VOICE_MAP.get(character.lower(), CHARACTER_VOICE_MAP["narrator"])
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.75, "similarity_boost": 0.75}
    }
    response = requests.post(url, headers=headers, json=data)
    with open(os.path.join(VOICES_DIR, filename), "wb") as f:
        f.write(response.content)

def parse_script(script_path):
    # Very basic: expects lines like "CHARACTER: dialogue"
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
        filename = f"{character.lower()}_line{idx+1}.mp3"
        tts_elevenlabs(character, dialogue, filename)
        print(f"Generated voice for {character}, line {idx+1}")