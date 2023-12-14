from PIL import Image, ImageEnhance, ImageOps
import os


# image = ImageOps.contain(image, (2048,2048))

def optimize_images(folder, height):
    logo = Image.open('logo_cropped.png')
    # os.chdir(folder)
    try:
        os.mkdir(f"{folder}\optimized")
    except:
        print("Toks katalogas jau yra")
    files = os.listdir(folder)
    for file in files:
        if file.endswith((".jpg", '.png')):
            pic = Image.open(f"{folder}\{file}")
            pic = ImageOps.contain(pic, (height, height))
            pic.paste(logo, (pic.size[0] - logo.size[0], pic.size[1] - logo.size[1], pic.size[0], pic.size[1]))
            pic.save()




optimize_images(r"C:\Users\donor\Desktop\nuotraukos", 500)