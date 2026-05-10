import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script(topic):
    print(f"Generating crime script for: {topic}")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """You are a professional true crime narrator and scriptwriter. 
                Your style is dark, suspenseful, dramatic and gripping.
                Write scripts that pull the listener in from the very first sentence.
                Use short punchy sentences for dramatic effect.
                Build tension slowly. Reveal details one by one.
                Write ONLY the exact words to be spoken out loud.
                No stage directions. No sound effects. No music cues.
                No labels like Narrator or Scene or Title.
                No brackets or parentheses.
                Write a full detailed script of at least 600 words.
                Just pure spoken words only, nothing else."""
            },
            {
                "role": "user",
                "content": f"Write a dramatic true crime narration script about: {topic}"
            }
        ]
    )

    script = response.choices[0].message.content
    print("Crime script generated successfully!")
    return script

if __name__ == "__main__":
    topic = "The mysterious disappearance of a young woman in Lagos"
    script = generate_script(topic)
    print("\n--- GENERATED SCRIPT ---")
    print(script)