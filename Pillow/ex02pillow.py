from PIL import Image, ImageDraw, ImageFont

preto = Image.new('RGB', (800, 800), (000, 000, 000))
branco = Image.new('RGB', (100, 100), (255, 255, 255))
h = 0
v = 0
for i in range(4):
    for j in range(4):
        preto.paste(branco, (h, v))
        h += 200

    v += 200
    h = 0
h = 100
v = 100
for i in range(4):
    for j in range(4):
        preto.paste(branco, (h, v))
        h += 200

    v += 200
    h = 100


preto.show()