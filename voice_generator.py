import pyttsx3
import os

def generate_voice(script, output_path="output/voiceover.wav"):
    print("Generating voiceover...")
    
    engine = pyttsx3.init()
    
    # Set voice properties
    engine.setProperty("rate", 150)    # speed
    engine.setProperty("volume", 1.0)  # volume
    
    # Get available voices and set English voice
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # 0 = male, 1 = female
    
    engine.save_to_file(script, output_path)
    engine.runAndWait()
    
    print(f"Voiceover saved to {output_path}")
    return output_path

if __name__ == "__main__":
    test_script = """
    Did you know that drinking water is one of the simplest and most effective ways 
    to boost your overall health and wellbeing? Staying hydrated can help boost your 
    energy levels, support healthy digestion, help with weight loss, keep your skin 
    healthy and radiant, and even reduce stress and anxiety. 
    Make it a habit to drink at least eight glasses of water a day 
    and experience the benefits for yourself. Stay hydrated, stay healthy.
    """
    generate_voice(test_script)