
from PIL import Image
img = Image.open('download (1).png')
print('Mode:', img.mode)
print('Size:', img.size)
if img.mode == 'RGBA':
    import numpy as np
    arr = __import__('numpy').array(img)
    print('TL alpha:', arr[0,0,3])
    print('TR alpha:', arr[0,-1,3])
