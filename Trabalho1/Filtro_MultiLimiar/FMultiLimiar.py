import cv2
import numpy as np
import matplotlib.pyplot as plt

img_in = cv2.imread('/Users/skoto/Documents/lena_color_256.tif', 0)
img_out = np.zeros(img_in.shape)

alt, larg = img_in.shape
flimiar1 = 80
flimiar2 = 160

for y in range(0, alt):
    for x in range(0, larg):
        if img_in[y,x] < flimiar1:
            img_out[y,x] = 255
        elif flimiar1 <= img_in[y,x] and img_in[y,x] < flimiar2:
            img_out[y,x] = 128
        elif img_in[y,x] >= flimiar2:
            img_out[y,x] = 0

img_out = np.uint8(img_out)

print(img_out)

plt.subplot(121), plt.imshow(img_in, 'gray')
plt.subplot(121).set_title('Imagem original')
plt.subplot(122), plt.imshow(img_out, 'gray')
plt.subplot(122).set_title('Imagem após multilimearização')

plt.show()
