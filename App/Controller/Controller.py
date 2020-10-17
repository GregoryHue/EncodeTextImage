import math

from PIL import Image
from App.Model import Model as model
from App.View import View as view


def EncodeTxtToImg(path):
    data = []

    txt = open(path, mode='r', encoding="utf-8")

    while True:
        char = txt.read(1)
        if char:
            if ord(char) <= 255:
                data.append(ord(char))
            else:
                view.ValueTooHIgh(ord(char))
        else:
            view.EndOfFile("txt")
            break
    txt.close()

    nb_pixels = math.ceil((len(data) / 4))
    h = math.ceil(math.sqrt(nb_pixels))
    w = math.ceil(math.sqrt(nb_pixels))

    img = Image.new('RGBA', (h, w), "black")
    pixelsColor = img.load()

    index = 0
    for j in range(img.size[0]):
        for i in range(img.size[1]):
            if index <= len(data) - 4:
                pixelsColor[i, j] = (data[index], data[index + 1], data[index + 2], data[index + 3])
                index += 4
            elif index == len(data) - 3:
                pixelsColor[i, j] = (data[index], data[index + 1], data[index + 2], 255)
                index += 3
            elif index == len(data) - 2:
                pixelsColor[i, j] = (data[index], data[index + 1], 0, 255)
                index += 2
            elif index == len(data) - 1:
                pixelsColor[i, j] = (data[index], 0, 0, 255)
                index += 1
            elif index == len(data):
                pixelsColor[i, j] = (0, 0, 0, 255)
            else:
                pass

    return img.save(model.GetFolderOfFile(path) + model.GetFileName(path) + "_Ncoded.png")


def DecodeImgToTxt(path):
    data = []
    img = Image.open(path)
    img.convert('RGBA')

    index = 0

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

    view.EndOfFile("png")

    txt = open(model.GetFolderOfFile(path) + model.GetFileName(path) + "_Dcoded.txt", mode="w+", encoding="utf-8")

    for i in data:
        txt.write(chr(i))

    txt.close()

    return txt
