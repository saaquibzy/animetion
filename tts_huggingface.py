import requests

def tts_suno(text, out_path="voices/voice1.wav", speaker="female"):
    url = "https://suno-tts.hf.space/run/predict"
    payload = {"data": [text, speaker]}
    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        audio_url = response.json()["data"][0]
        audio = requests.get(audio_url)
        with open(out_path, "wb") as f:
            f.write(audio.content)
        print(f"🔊 Voice generated and saved to {out_path}")
        return out_path
    except Exception as e:
        print("Error generating voice:", e)
        return None