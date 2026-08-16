import os
from PIL import Image

dirs = [
    r"c:\mesaweb\assets\images\meetourteams 2026-2027",
    r"c:\mesaweb\assets\images\halloffame 2025-2026"
]

for d in dirs:
    if not os.path.exists(d):
        continue
    for filename in os.listdir(d):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(d, filename)
            try:
                with Image.open(filepath) as img:
                    # Rotate 180 degrees (flip completely upside down/right side up)
                    rotated = img.transpose(Image.ROTATE_180)
                    rotated.save(filepath, format="JPEG", quality=85)
                print(f"Flipped 180: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
