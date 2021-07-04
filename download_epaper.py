import requests
import shutil
from datetime import datetime

today = datetime.now()
dt = today.strftime("%d%m%Y")
img_pre = (
    "https://epaper.anandabazar.com/epaperimages////" + dt + "////" + dt + "-md-hr-"
)
img_post = "ll.png"

i = 1
image_url = img_pre + str(i) + img_post
r = requests.get(image_url, stream=True)
while r.status_code == 200:
    r.raw.decode_content = True
    filename = dt + "_" + str(i) + ".png"
    with open(filename, "wb") as f:
        shutil.copyfileobj(r.raw, f)
    i += 1
    image_url = img_pre + str(i) + img_post
    r = requests.get(image_url, stream=True, allow_redirects=False)
