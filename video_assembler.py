from moviepy import AudioFileClip, VideoClip, concatenate_videoclips
from PIL import Image
import numpy as np
import os

def ken_burns_clip(image_path, duration, effect="zoom_in"):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((1280, 720), Image.LANCZOS)
    img_array = np.array(img)

    def make_frame(t):
        progress = t / duration

        if effect == "zoom_in":
            scale = 1.0 + 0.15 * progress
        elif effect == "zoom_out":
            scale = 1.15 - 0.15 * progress
        elif effect == "pan_right":
            scale = 1.10
        elif effect == "pan_left":
            scale = 1.10
        else:
            scale = 1.0

        new_w = int(1280 * scale)
        new_h = int(720 * scale)

        resized = np.array(
            Image.fromarray(img_array).resize((new_w, new_h), Image.LANCZOS)
        )

        if effect == "pan_right":
            x_start = int((new_w - 1280) * progress)
            y_start = (new_h - 720) // 2
        elif effect == "pan_left":
            x_start = int((new_w - 1280) * (1 - progress))
            y_start = (new_h - 720) // 2
        else:
            x_start = (new_w - 1280) // 2
            y_start = (new_h - 720) // 2

        frame = resized[y_start:y_start+720, x_start:x_start+1280]
        return frame

    clip = VideoClip(make_frame, duration=duration)
    return clip

def assemble_video(image_paths, audio_path, output_path="output/final_video.mp4"):
    print("Assembling cinematic crime video...")

    audio = AudioFileClip(audio_path)
    total_duration = audio.duration

    scene_duration = total_duration / len(image_paths)

    print(f"Total duration: {total_duration:.1f}s")
    print(f"Each scene duration: {scene_duration:.1f}s")

    effects = ["zoom_in", "zoom_out", "pan_right", "pan_left"]

    clips = []
    for i, image_path in enumerate(image_paths):
        effect = effects[i % len(effects)]
        print(f"Applying {effect} to scene {i+1}...")
        clip = ken_burns_clip(image_path, scene_duration, effect=effect)
        clips.append(clip)

    final_video = concatenate_videoclips(clips, method="compose")
    final_video.audio = audio

    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="pcm_s16le",
        temp_audiofile="output/temp_audio.wav",
        remove_temp=True
    )

    print(f"Cinematic video saved to {output_path}")
    return output_path

if __name__ == "__main__":
    image_paths = ["output/backgrounds/lucid-origin_a_cinematic_photo_of_Cinematic_3D_animated_scene_young_African_Nigerian_woman_wa-0.jpg"]
    audio_path = "output/voiceover.wav"
    assemble_video(image_paths, audio_path)