from PIL import Image
import numpy as np
img = Image.open('/root/pc3-speedfix/circle-logo-TRUE.png')
arr = np.array(img)
print('Mode:', img.mode)
print('Size:', img.size)
print('Corner pixel RGBA:', arr[0,0].tolist())
print('Center pixel RGBA:', arr[img.size[1]//2, img.size[0]//2].tolist())
if img.mode == 'RGBA':
    alpha = arr[:,:,3]
    print('Alpha min:', alpha.min())
    print('Alpha max:', alpha.max())
    print('Fully transparent pixels:', (alpha==0).sum())
