
from PIL import Image

im = Image.open("logo.png")

region = im.crop((0, 28, 128, 100))

region.save("logo_cropped.png")