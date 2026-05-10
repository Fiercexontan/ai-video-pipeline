import pyttsx3
import os

def generate_voice(script, output_path="output/voiceover.wav"):
    print("Generating crime narration voice...")

    engine = pyttsx3.init()

    # Deep slow dramatic voice settings
    engine.setProperty("rate", 125)      # slower = more dramatic
    engine.setProperty("volume", 1.0)

    # Set deep male voice
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  # 0 = male deep voice

    engine.save_to_file(script, output_path)
    engine.runAndWait()

    print(f"Narration saved to {output_path}")
    return output_path

if __name__ == "__main__":
    test_script = """
    It was a night like any other in Lagos.
    Nobody suspected what was about to happen.
    She left home at 7pm. And never came back.
    Her phone went silent.
    Her family waited all night.
    By morning, the panic had set in.
    The streets held a dark secret.
    Nobody was ready to face the truth.
    Nothing is as it seems in this city of shadows.
    """
    generate_voice(test_script)