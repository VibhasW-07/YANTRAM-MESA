import os
from PIL import Image

dir_path = r"c:\mesaweb\assets\images\halloffame 2025-2026"
files_to_fix = [
    "Aditya Tambe Marketing Head.jpeg",
    "Tanvi Yendhe Marketing Head.jpeg"
]

for filename in files_to_fix:
    filepath = os.path.join(dir_path, filename)
    if os.path.exists(filepath):
        try:
            with Image.open(filepath) as img:
                # Heads are pointing left, so we need to rotate 90 degrees clockwise (ROTATE_270 in Pillow)
                rotated = img.transpose(Image.ROTATE_270)
                rotated.save(filepath, format="JPEG", quality=85)
            print(f"Fixed rotation for: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    else:
        print(f"File not found: {filepath}")
