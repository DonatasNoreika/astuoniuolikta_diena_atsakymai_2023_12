from PIL import Image

def turn_binary(image, r, g, b):
    im = Image.open(image)
    data = im.getdata()
    new_data = []
    black = (0, 0, 0)
    white = (255, 255, 255)
    for pixel in data:
        if pixel[0] >= r or pixel[1] >= g or pixel[2] >= b:
            new_data.append(white)
        else:
            new_data.append(black)
    im.putdata(new_data)
    im.show()
    return im


turn_binary("cat.jpg", 100, 200, 200)