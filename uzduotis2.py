from PIL import Image, ImageEnhance
import os


def enhance_image(picture, contrast, color, sharpness, brightness, save=False):
    im = Image.open(picture)
    im = ImageEnhance.Contrast(im).enhance(contrast)
    im = ImageEnhance.Color(im).enhance(color)
    im = ImageEnhance.Sharpness(im).enhance(sharpness)
    im = ImageEnhance.Brightness(im).enhance(brightness)
    im.show()
    if save:
        loc = os.path.splitext(picture)[0]
        ext = os.path.splitext(picture)[1]
        im.save(f"{loc}_modified{ext}")


enhance_image("Porsche Taycan.jpg", 2, 1.5, 1.5, 1, True)
# enhance_image("cat.jpg", 0.5, 0.5, 1.5, 1.5)
