import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script(topic):
    print(f"Generating script for: {topic}")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """You are a professional video script writer. 
Write ONLY the exact words to be spoken out loud. 
No stage directions. No sound effects. No music cues. 
No labels like 'Narrator:' or 'Scene:' or 'Title:'.
No brackets or parentheses.
Just pure spoken words only, nothing else."""
            },
            {
                "role": "user",
                "content": f"Write a video script about: {topic}"
            }
        ]
    )

    script = response.choices[0].message.content
    print("Script generated successfully!")
    return script

if __name__ == "__main__":
    topic = "The benefits of drinking water daily"
    script = generate_script(topic)
    print("\n--- GENERATED SCRIPT ---")
    print(script)