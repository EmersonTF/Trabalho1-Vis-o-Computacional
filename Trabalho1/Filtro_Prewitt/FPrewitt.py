import cv2
import numpy as np
import matplotlib.pyplot as plt

img_in = cv2.imread('/Users/skoto/Documents/lena_color_256.tif', 0)
img_out = np.ones(img_in.shape)

alt, larg = img_in.shape

for y in range(0, alt):
    for x in range(0, larg):
        if x>0 and y>0 and x<(larg-1) and y<(alt-1):
            Gx = (((-1)*int(img_in[y-1][x-1]))+(0*int(img_in[y-1][x]))+int(img_in[y-1][x+1])
                    +((-1)*int(img_in[y][x-1]))+(0*int(img_in[y][x]))+int(img_in[y][x+1])
                    +((-1)*int(img_in[y+1][x-1]))+(0*int(img_in[y+1][x]))+int(img_in[y+1][x+1]))

            Gy = (((-1)*int(img_in[y-1][x-1]))+((-1)*int(img_in[y-1][x]))+((-1)*int(img_in[y-1][x+1]))
                    +(0*int(img_in[y][x-1]))+(0*int(img_in[y][x]))+(0*int(img_in[y][x+1]))
                    +int(img_in[y+1][x-1])+int(img_in[y+1][x])+int(img_in[y+1][x+1]))

            img_out[y,x] = np.sqrt((Gx**2 + Gy**2))
            if img_out[y,x] > 255:
                img_out[y,x] = 255
            elif img_out[y,x] < 0:
                img_out[y,x] = 0            
        else:
            img_out[y,x] = 0

img_out = np.uint8(img_out)

print(img_out)

plt.subplot(121), plt.imshow(img_in, 'gray')
plt.subplot(121).set_title('Imagem original')
plt.subplot(122), plt.imshow(img_out, 'gray')
plt.subplot(122).set_title('Imagem após aplicar o filtro de Prewitt')

plt.show()
