import cv2
import numpy as np
import matplotlib.pyplot as plt

img_in = cv2.imread('/Users/skoto/Documents/lena_color_256.tif', 0)
alt, larg = img_in.shape
C_hist_ = np.zeros(larg)


for y in range(0, alt):
    for x in range(0, larg):
            C_hist_[(img_in[y,x])] += 1

print(C_hist_)

plt.subplot(121), plt.imshow(img_in, 'gray')
plt.subplot(121).set_title('Imagem original')
plt.subplot(122), plt.stem(C_hist_)
plt.subplot(122).set_title('Histograma da imagem')

plt.show()
