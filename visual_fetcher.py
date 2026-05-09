from PIL import Image, ImageDraw, ImageFont
import os

COLORS = [
    "#1a1a2e", "#16213e", "#0f3460",
    "#533483", "#2b2d42", "#1b4332",
    "#212529", "#343a40", "#003049"
]

def split_script_into_scenes(script):
    sentences = []
    for line in script.split("\n"):
        line = line.strip()
        if line:
            parts = line.split(". ")
            for part in parts:
                part = part.strip()
                if len(part) > 10:
                    sentences.append(part)
    return sentences

def wrap_text(text, max_chars=40):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            current += (" " if current else "") + word
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def create_scene_image(text, color, index, output_folder):
    img = Image.new("RGB", (1280, 720), color=color)
    draw = ImageDraw.Draw(img)

    # Draw scene number
    draw.text((60, 50), f"[ {index+1} ]", fill="#ffffff")

    # Draw main text centered and wrapped
    lines = wrap_text(text, max_chars=45)
    line_height = 80
    total_height = len(lines) * line_height
    start_y = (720 - total_height) // 2

    for i, line in enumerate(lines):
        y = start_y + i * line_height
        draw.text((640, y), line, fill="#ffffff", anchor="mm")

    # Draw bottom bar
    draw.rectangle([0, 680, 1280, 720], fill="#ffffff22")

    path = f"{output_folder}/scene_{index+1}.png"
    img.save(path)
    return path

def fetch_videos(topic, script=None, output_folder="output/clips"):
    print(f"Generating animated scenes for: {topic}")
    os.makedirs(output_folder, exist_ok=True)

    if script:
        scenes = split_script_into_scenes(script)
    else:
        scenes = [
            f"Welcome to this video about {topic}",
            f"Let's explore {topic} together",
            f"Here are the key facts about {topic}",
            f"Thank you for watching!"
        ]

    image_paths = []
    for i, scene_text in enumerate(scenes):
        color = COLORS[i % len(COLORS)]
        path = create_scene_image(scene_text, color, i, output_folder)
        print(f"Scene {i+1} created: {scene_text[:50]}...")
        image_paths.append(path)

    print(f"All {len(image_paths)} scenes generated!")
    return image_paths

if __name__ == "__main__":
    topic = "benefits of drinking water"
    test_script = """
    Did you know that drinking water is one of the simplest ways to boost your health?
    Staying hydrated helps boost your energy levels throughout the day.
    Water supports healthy digestion and helps absorb nutrients.
    Drinking enough water can help support weight loss goals.
    Water keeps your skin healthy, radiant and young looking.
    Make it a habit to drink at least eight glasses of water a day.
    Stay hydrated. Stay healthy.
    """
    fetch_videos(topic, script=test_script)