from os import path
from PIL import Image
from datetime import datetime

today = datetime.now()
dt = today.strftime("%d%m%Y")

all_images = []
idx = 2
img1 = Image.open(f"{dt}_1.png")

while path.exists(fname := dt + "_" + str(idx) + ".png"):
    image = Image.open(fname)
    img = image.convert("RGB")
    all_images.append(img)
    idx += 1

img1.save(f"paper_{dt}.pdf", save_all=True, append_images=all_images)
