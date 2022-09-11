import cv2
import numpy as np
import matplotlib.pyplot as plt

img_in = cv2.imread('/Users/skoto/Documents/lena_color_256.tif', 0)
img_out = np.ones(img_in.shape)

alt, larg = img_in.shape

for y in range(0, alt):
    for x in range(0, larg):
        if x>0 and y>0 and x<(larg-2) and y<(alt-2):
            img_out[y,x] = (int(img_in[y-2][x-2])+(4*int(img_in[y-2][x-1]))+(7*int(img_in[y-2][x]))+int(4*(img_in[y-2][x+1]))+int(img_in[y-2][x+2])
                            +(4*int(img_in[y-1][x-2]))+(16*int(img_in[y-2][x-1]))+(26*int(img_in[y-1][x]))+(16*int(img_in[y-1][x+1]))+(4*int(img_in[y-1][x+2]))
                            +(7*int(img_in[y][x-2]))+(26*int(img_in[y][x-1]))+(41*int(img_in[y][x]))+(26*int(img_in[y][x+1]))+(7*int(img_in[y][x+2]))
                            +(4*int(img_in[y+1][x-2]))+(16*int(img_in[y+1][x-1]))+(26*int(img_in[y+1][x]))+(16*int(img_in[y+1][x+1]))+(4*int(img_in[y+1][x+2]))
                            +int(img_in[y+2][x-2])+(4*int(img_in[y+2][x-1]))+(7*int(img_in[y+2][x]))+(4*int(img_in[y+2][x+1]))+int(img_in[y+2][x+2]))/273
        else:
            img_out[y,x] = 0

img_out = np.uint8(img_out)

print(img_out)

plt.subplot(121), plt.imshow(img_in, 'gray')
plt.subplot(121).set_title('Imagem original')
plt.subplot(122), plt.imshow(img_out, 'gray')
plt.subplot(122).set_title('Imagem após aplicar o filtro Gaussiano')

plt.show()
