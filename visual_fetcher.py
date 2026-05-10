import os

def fetch_videos(topic, script=None, output_folder="output/backgrounds"):
    print(f"Loading crime scene images for: {topic}")

    image_paths = []

    files = sorted([
        f for f in os.listdir(output_folder)
        if f.endswith((".png", ".jpg", ".jpeg"))
    ])

    if not files:
        print("No images found in output/backgrounds folder!")
        return []

    for file in files:
        full_path = os.path.join(output_folder, file)
        image_paths.append(full_path)
        print(f"Loaded: {file}")

    print(f"Total images loaded: {len(image_paths)}")
    return image_paths

if __name__ == "__main__":
    images = fetch_videos("Lagos mystery")
    for img in images:
        print(img)