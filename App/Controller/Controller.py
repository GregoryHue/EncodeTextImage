import math

from PIL import Image
from App.Model import Model as Model
from App.View import View as View


def EncodeTxtToImg(path):
    data = []

    txt = open(path, mode='r', encoding="utf-8")

    while True:
        char = txt.read(1)
        if char:
            if ord(char) <= 255:
                data.append(ord(char))
            else:
                View.ValueTooHIgh(ord(char))
        else:
            View.EndOfFile("txt")
            break
    txt.close()

    nb_pixels = math.ceil((len(data) / 4))
    h = math.ceil(math.sqrt(nb_pixels))
    w = math.ceil(math.sqrt(nb_pixels))

    img = Image.new('RGBA', (h, w), "black")
    pixels_color = img.load()

    index = 0
    for j in range(img.size[0]):
        for i in range(img.size[1]):
            if index <= len(data) - 4:
                pixels_color[i, j] = (data[index], data[index + 1], data[index + 2], data[index + 3])
                index += 4
            elif index == len(data) - 3:
                pixels_color[i, j] = (data[index], data[index + 1], data[index + 2], 255)
                index += 3
            elif index == len(data) - 2:
                pixels_color[i, j] = (data[index], data[index + 1], 0, 255)
                index += 2
            elif index == len(data) - 1:
                pixels_color[i, j] = (data[index], 0, 0, 255)
                index += 1
            elif index == len(data):
                pixels_color[i, j] = (0, 0, 0, 255)
            else:
                pass

    return img.save(Model.GetFolderOfFile(path) + Model.GetFileName(path) + "_Ncoded.png")


def DecodeImgToTxt(path):
    data = []
    img = Image.open(path)
    img.convert('RGBA')

    for j in range(img.size[0]):
        for i in range(img.size[1]):
            r, g, b, a = img.getpixel((i, j))
            if r != 0:
                data.append(r)
            if g != 0:
                data.append(g)
            if b != 0:
                data.append(b)
            if a != 255:
                data.append(a)

    View.EndOfFile("png")

    txt = open(Model.GetFolderOfFile(path) + Model.GetFileName(path) + "_Dcoded.txt", mode="w+", encoding="utf-8")

    for i in data:
        txt.write(chr(i))

    txt.close()

    return txt
