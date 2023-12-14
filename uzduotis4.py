from PIL import Image

def ribos(sk):
    if sk > 255:
        return 255
    if sk < 0:
        return 0
    return sk

def adjust_colors(picture, r: int, g: int, b: int):
    im = Image.open(picture)
    data = im.getdata()
    new_data = []
    for pixel in data:
        red = ribos(pixel[0] + r)
        green = ribos(pixel[1] + g)
        blue = ribos(pixel[2] + b)
        new_data.append((red, green, blue))
    im.putdata(new_data)
    im.show()



# adjust_colors("dog.jpg", 50, 0, -50)

adjust_colors("Porsche Taycan.jpg", -150, -250, -150)