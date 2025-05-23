# video_editor.py

import os
from moviepy.editor import concatenate_videoclips, TextClip, CompositeVideoClip, VideoFileClip, AudioFileClip
from config import ANIMATIONS_DIR, VIDEOS_DIR

def merge_clips_with_subtitles(clip_files, subtitles, output_file, music_file=None):
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    clips = []
    for idx, clip_path in enumerate(clip_files):
        video = VideoFileClip(clip_path)
        # Overlay subtitles if given
        if subtitles and idx < len(subtitles):
            txt = subtitles[idx]
            txt_clip = TextClip(txt, fontsize=40, color='white', bg_color='black', size=(video.w, 100))
            txt_clip = txt_clip.set_duration(video.duration).set_position(('center', 'bottom'))
            composite = CompositeVideoClip([video, txt_clip])
            clips.append(composite)
        else:
            clips.append(video)
    final = concatenate_videoclips(clips, method="compose")
    # Add background music if provided
    if music_file and os.path.exists(music_file):
        music = AudioFileClip(music_file).volumex(0.15)
        final = final.set_audio(music)
    final.write_videofile(os.path.join(VIDEOS_DIR, output_file), fps=24, codec='libx264', audio_codec='aac', threads=4)

if __name__ == "__main__":
    # Example: merge all animations with dummy subtitles
    clip_files = [os.path.join(ANIMATIONS_DIR, f) for f in sorted(os.listdir(ANIMATIONS_DIR)) if f.endswith(".mp4")]
    subtitles = [f"Line {i+1}" for i in range(len(clip_files))]
    merge_clips_with_subtitles(clip_files, subtitles, "final_reel.mp4")
    print("Merged video saved as final_reel.mp4")