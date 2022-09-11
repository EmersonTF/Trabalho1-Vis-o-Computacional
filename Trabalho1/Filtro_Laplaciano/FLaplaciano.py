import cv2
import numpy as np
import matplotlib.pyplot as plt

img_in = cv2.imread('/Users/skoto/Documents/lena_color_256.tif', 0)
img_out = np.ones(img_in.shape)
mascara = np.array([-1,-1,-1,-1,8,-1,-1,-1,-1]).reshape(3,3)

alt, larg = img_in.shape

for y in range(0, alt):
    for x in range(0, larg):
        if x>0 and y>0 and x<(larg-1) and y<(alt-1):
            img_out[y,x] = ((int(img_in[y-1][x-1])*mascara[0][0])+(int(img_in[y-1][x])*mascara[0][1])+(int(img_in[y-1][x+1])*mascara[0][2])
                            +(int(img_in[y][x-1])*mascara[1][0])+(int(img_in[y][x])*mascara[1][1])+(int(img_in[y][x+1])*mascara[1][2])
                            +(int(img_in[y+1][x-1])*mascara[2][0])+(int(img_in[y+1][x])*mascara[2][1])+(int(img_in[y+1][x+1])*mascara[2][2]))
            if img_out[y,x] > 255:
                img_out[y,x] = 255
            elif img_out[y,x] < 0:
                img_out[y,x] = 0
                            
        else:
            img_out[y,x] = 0

print(img_out)

plt.subplot(121), plt.imshow(img_in, 'gray')
plt.subplot(121).set_title('Imagem original')
plt.subplot(122), plt.imshow(img_out, 'gray')
plt.subplot(122).set_title('Imagem após aplicar o filtro Laplaciano')

plt.show()
