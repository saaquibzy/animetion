# animation_bot.py

import os
import subprocess
from config import VOICES_DIR, ANIMATIONS_DIR
from character_image_manager import get_or_generate_character_image

def animate_with_wav2lip(character, voice_file, output_file):
    # Assumes Wav2Lip is installed and available via command line
    # You need a face image and a voice file (mp3/wav)
    img_path = get_or_generate_character_image(character)
    os.makedirs(ANIMATIONS_DIR, exist_ok=True)
    output_path = os.path.join(ANIMATIONS_DIR, output_file)
    cmd = [
        "python", "Wav2Lip/inference.py",
        "--checkpoint_path", "Wav2Lip/checkpoints/wav2lip_gan.pth",
        "--face", img_path,
        "--audio", voice_file,
        "--outfile", output_path,
        "--pads", "0", "20", "0", "0"
    ]
    subprocess.run(cmd, check=True)
    return output_path

if __name__ == "__main__":
    # Animate all voices
    for file in os.listdir(VOICES_DIR):
        if file.endswith(".mp3"):
            character = file.split("_")[0]
            voice_path = os.path.join(VOICES_DIR, file)
            output_file = f"{character}_{file.replace('.mp3', '.mp4')}"
            animate_with_wav2lip(character, voice_path, output_file)
            print(f"Animated {character}: {output_file}")
            