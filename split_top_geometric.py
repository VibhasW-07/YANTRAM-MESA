from PIL import Image

img = Image.open('assets/images/sponsors_grid.jpeg')
# Crop y=150 to y=344 (150+194)
top_crop = img.crop((0, 150, img.width, 344))

# Bounding box is x=33 to 904. Width=871.
w = 871 // 3
y1 = 0
y2 = 194

# Monster
monster = top_crop.crop((33, y1, 33 + w, y2))
monster.save('assets/images/sponsors/sponsor_monster.png')

# Vivo
vivo = top_crop.crop((33 + w, y1, 33 + w*2, y2))
vivo.save('assets/images/sponsors/sponsor_vivo.png')

# Oppo
oppo = top_crop.crop((33 + w*2, y1, 33 + w*3, y2))
oppo.save('assets/images/sponsors/sponsor_oppo.png')

print("Saved top 3 logos!")
