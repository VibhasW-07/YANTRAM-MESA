import os
from PIL import Image, ImageOps

dirs = [
    r"c:\mesaweb\assets\images\meetourteams 2026-2027",
    r"c:\mesaweb\assets\images\halloffame 2025-2026"
]

MAX_SIZE = 800

for d in dirs:
    if not os.path.exists(d):
        continue
    for filename in os.listdir(d):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(d, filename)
            try:
                with Image.open(filepath) as img:
                    # Fix EXIF orientation before any other processing
                    img = ImageOps.exif_transpose(img)
                    
                    # Convert to RGB if needed
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Resize if larger than MAX_SIZE
                    if img.width > MAX_SIZE or img.height > MAX_SIZE:
                        img.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)
                    
                    # Save over the original file
                    img.save(filepath, format="JPEG", quality=70, optimize=True)
                print(f"Compressed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
