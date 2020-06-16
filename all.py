import math
from PIL import Image

data = []
nb_pixels = 0
h = 0
w = 0

error = False

fin = open('intxt.txt', 'r')

while True:
    c = fin.read(1)
    if c:
        if ord(c) <= 255:
            data.append(ord(c))
            print(c + '; ' + str(ord(c)))
        else:
            error = True
    else:
        print("End of file")
        break
fin.close()
print(error)
print(data)
print(len(data))
nb_pixels = math.ceil((len(data) / 4))
h = math.ceil(math.sqrt(nb_pixels))
w = math.ceil(math.sqrt(nb_pixels))
print(nb_pixels)
print(h)
print(w)
print(h * w)


img = Image.new( 'RGBA', (h, w), "black")
pixels = img.load()
index = 0

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if index <= len(data) - 4:
            pixels[i, j] = (data[index], data[index+1], data[index+2], data[index+3])
            index += 4

img.save("png.png")

databack = []
imgback = Image.open("png.png")
imgback.convert('RGB')

for i in range(imgback.size[0]):
    for j in range(imgback.size[1]):
        r, g, b, a = imgback.getpixel((i, j))
        if r != 0 and g != 0 and b != 0 and a != 255:
            databack.append(a)
            databack.append(r)
            databack.append(g)
            databack.append(b)

fout = open("outtxt.txt", "w+")

print(databack)
for i in databack:
    print(chr(i), end='')
    fout.write(chr(i))

fout.close()

print("END")