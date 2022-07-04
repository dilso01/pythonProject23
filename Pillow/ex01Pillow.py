from PIL import Image, ImageDraw, ImageFont

azul = Image.new('RGB', (600, 400), (000, 000, 255))
branco = Image.new('RGB', (400, 400), (255, 255, 255))
vermelho = Image.new('RGB', (200, 400), (255, 000, 000))

azul.paste(branco, (200, 0))
azul.paste(vermelho, (400, 0))

azul.show()
