from PIL import Image

img = Image.open('assets/images/sponsors/sponsor_5.png')
w, h = img.size

# A.I.I.I.T.S (top left)
aiiits = img.crop((0, 0, w//2, h//2 + 20))
aiiits.save('assets/images/sponsors/sponsor_aiiits.png')

# IMFS (top right)
imfs = img.crop((w//2, 0, w, h//2 + 20))
imfs.save('assets/images/sponsors/sponsor_imfs.png')

# Dhaaga (bottom center)
dhaaga = img.crop((0, h//2, w, h))
dhaaga.save('assets/images/sponsors/sponsor_dhaaga.png')

print("Saved geometric crops!")
