import os
from PIL import Image, ImageOps

d = r"c:\mesaweb\assets\images"
MAX_SIZE = 1200

for filename in ["Introductionmesa.jpeg", "ROLEmesa.JPG", "whoweare.JPG"]:
    filepath = os.path.join(d, filename)
    try:
        with Image.open(filepath) as img:
            img = ImageOps.exif_transpose(img)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            if img.width > MAX_SIZE or img.height > MAX_SIZE:
                img.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)
            img.save(filepath, format="JPEG", quality=75, optimize=True)
        print(f"Compressed: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
