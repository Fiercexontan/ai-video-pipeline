import os
from script_generator import generate_script
from voice_generator import generate_voice
from visual_fetcher import fetch_videos
from video_assembler import assemble_video

def main():
    print("=" * 50)
    print("   AI VIDEO PIPELINE - BY LINCOLN")
    print("=" * 50)

    # Step 1 - Get topic from user
    topic = input("\nEnter your video topic: ")

    print("\n[1/4] Generating script...")
    script = generate_script(topic)
    print("\n--- SCRIPT PREVIEW ---")
    print(script[:300] + "...")

    print("\n[2/4] Generating voiceover...")
    audio_path = generate_voice(script)

    print("\n[3/4] Creating visual scenes...")
    image_paths = fetch_videos(topic, script=script)

    print("\n[4/4] Assembling final video...")
    video_path = assemble_video(image_paths, audio_path)

    print("\n" + "=" * 50)
    print(f"VIDEO COMPLETE!")
    print(f"Saved to: {video_path}")
    print("=" * 50)

if __name__ == "__main__":
    main()