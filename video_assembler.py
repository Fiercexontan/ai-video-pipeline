from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
import os

def assemble_video(image_paths, audio_path, output_path="output/final_video.mp4"):
    print("Assembling final video...")

    # Load audio
    audio = AudioFileClip(audio_path)
    total_duration = audio.duration

    # Each scene gets equal time
    scene_duration = total_duration / len(image_paths)

    print(f"Total duration: {total_duration:.1f}s")
    print(f"Each scene duration: {scene_duration:.1f}s")

    # Create video clips from images
    clips = []
    for i, image_path in enumerate(image_paths):
        clip = ImageClip(image_path, duration=scene_duration)
        clips.append(clip)
        print(f"Scene {i+1} added...")

    # Combine all clips
    final_video = concatenate_videoclips(clips, method="compose")

    # Set audio duration to match video
    audio = audio.with_duration(final_video.duration)

    # Set audio on video
    final_video.audio = audio

    # Export final video
    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="pcm_s16le",
        temp_audiofile="output/temp_audio.wav",
        remove_temp=True
    )

    print(f"Final video saved to {output_path}")
    return output_path

if __name__ == "__main__":
    image_paths = [
        f"output/clips/scene_{i+1}.png" for i in range(8)
    ]
    audio_path = "output/voiceover.wav"
    assemble_video(image_paths, audio_path)