from PIL import Image, ImageDraw, ImageFont
from time import sleep
# carregar ou importar uma imagem
# im = Image.open('cão.png')
# im.show()

# converter a cor da imagem

# im = Image.open('cão.png')
# im = im.convert("1")
# im.show()
#
# #
# im = Image.open('cão.png')
# im = im.convert("L")
# im.show()

# descobrir o tamanho da imagem

# im = Image.open('cão.png')
# print(im.size)
# x, y = im.size
# im.show()

# criar uma imagem do zero
#
# im = Image.new('RGB', (150, 150), (230, 162, 200))
# im.save("imagem.jpg")
# im.show()

#  Criar uma imagem dividida em dois

# im = Image.new('RGB', (150, 150), (0, 0, 0))
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         if i < x // 2:
#             im.putpixel((i, j), (255, 255, 255))
# im2 = ImageDraw.Draw(im)
# im2.ellipse((x//2-50, y//2-50, x//2+50, y//2+50), fill=(0, 0, 255))
#
# im.show()

# Trocar o valor das cores das imagens
# im. = Image.open('cão.png')
# x, y = im.size
# im.show(
# for i in range(x):
#     for j in range(y):
#         r, g, b = im.getpixel()
#             print(r, g, b)

#  getpixel pega a cor da imagem, putpixel troca a cor da imagem

# outline= 0,0,0 dita o contorno na imagem
#
# comprimir a imagem

# criar uma mascara
im1 = Image.open('cão.png')
im2 = Image.open('PNG_transparency_demonstration_1.png')
mask = Image.new('L', im1.size)
# draw.rectangle((0, 0, 427, 327), fill=255)
im = Image.composite(im1, im2, mask)
im.show()
sleep(2)
im.close()
# como escrever na imagem
# local C:\Windows\Fonts\ALGER
#

# image = Image.open(r'cão.png')
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype(r'C:\Windows\Fonts\ALGER', 20)
# text = 'PAISAGEM'
# draw.text((10, 10), text, font=font, fill=(25, 100, 255))
# image.show()

