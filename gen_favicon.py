
from PIL import Image

src = Image.open('favicon-source-final.png').convert('RGBA')
print('Source size:', src.size)
print('Corner pixel 0,0:', src.getpixel((0,0)))
print('Center pixel:', src.getpixel((512,512)))

for size, name in [(16, 'favicon-16x16.png'), (32, 'favicon-32x32.png'), (180, 'apple-touch-icon.png')]:
    resized = src.resize((size, size), Image.LANCZOS)
    resized.save(name, 'PNG')
    check = Image.open(name).convert('RGBA')
    print(f'{name}: corner={check.getpixel((0,0))}, center={check.getpixel((size//2, size//2))}')

sizes = [(16,16),(32,32),(48,48)]
imgs = [src.resize((w,h), Image.LANCZOS) for w,h in sizes]
imgs[0].save('favicon.ico', format='ICO', sizes=sizes)
print('favicon.ico done')
