# pipeline_controller.py

import os
from script_generator import generate_script
from voice_generator import parse_script, tts_elevenlabs
from animation_bot import animate_with_wav2lip
from video_editor import merge_clips_with_subtitles
from config import VOICES_DIR, ANIMATIONS_DIR, VIDEOS_DIR

def pipeline(topic="Teenage love, funny, school romance", music_file=None):
    # 1. Script generation
    script = generate_script(topic)
    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)
    print("[1/5] Script generated.")

    # 2. Voice generation
    os.makedirs(VOICES_DIR, exist_ok=True)
    script_lines = parse_script("script.txt")
    for character, dialogue, idx in script_lines:
        filename = f"{character.lower()}_line{idx+1}.mp3"
        tts_elevenlabs(character, dialogue, filename)
    print("[2/5] Voice lines generated.")

    # 3. Animation
    os.makedirs(ANIMATIONS_DIR, exist_ok=True)
    clip_files = []
    subtitles = []
    for character, dialogue, idx in script_lines:
        voice_file = os.path.join(VOICES_DIR, f"{character.lower()}_line{idx+1}.mp3")
        output_file = f"{character.lower()}_line{idx+1}.mp4"
        clip_path = animate_with_wav2lip(character, voice_file, output_file)
        clip_files.append(clip_path)
        subtitles.append(dialogue)
    print("[3/5] Animations generated.")

    # 4. Video editing
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    merge_clips_with_subtitles(clip_files, subtitles, "final_reel.mp4", music_file)
    print(f"[4/5] Final video created: {os.path.join(VIDEOS_DIR, 'final_reel.mp4')}")
    print("[5/5] Upload to Instagram manually. Done!")

if __name__ == "__main__":
    # Run the full pipeline
    pipeline()