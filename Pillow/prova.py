from PIL import Image, ImageDraw, ImageFonte
# im = Image.new("RGB", (50, 50), (255, 0, 0))
# print(im.getpixel((14, 62)))

im = Image.new('RGB', (500, 500), (255, 255, 255))
joinha = Image.open('joinha.png')
joinha = joinha.resize((150, 150))
tamanho_x, tamanho_y = joinha.size\
joinha.ellipse((x//2-50, y//2-50, x//2+50, y//2+50), fill=(0, 0, 255))
im.show()

# azul = Image.new('RGB', (400, 200), (000, 000, 255))
# draw = ImageDraw.Draw(azul)
# font = ImageFont.truetype(r'C:\Windows\Fonts\ALGER', 40)
#
# text = 'ADILSON'
# draw.text((25, 25), text, font=font, fill=(255, 255, 255))
#
# azul.show()