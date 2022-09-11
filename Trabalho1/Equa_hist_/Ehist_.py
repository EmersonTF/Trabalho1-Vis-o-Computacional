import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as m

img_in = cv2.imread('/Users/skoto/Documents/lena_color_256.tif', 0)
img_out = np.zeros(img_in.shape)
alt, larg = img_in.shape
C_hist_ = np.zeros(256)
C2_hist_ = np.zeros(256)
E_hist_ = np.zeros(256)
a = m.ceil(255/(larg*alt))

for y in range(0, alt):
    for x in range(0, larg):
        C_hist_[(img_in[y,x])] += 1

E_hist_[0] = a*C_hist_[0]

for i in range(1, 255):
    E_hist_[i] = E_hist_[i-1]+a*C_hist_[i]

for y in range(0, alt):
    for x in range(0, larg):
        img_out[y,x] = E_hist_[img_in[y,x]]/255

img_out = np.uint8(img_out)

for y in range(0, alt):
    for x in range(0, larg):
        C2_hist_[(img_out[y,x])] += 1

plt.figure(1)
plt.subplot(121), plt.imshow(img_in, 'gray')
plt.subplot(121).set_title('Imagem original')
plt.subplot(122), plt.stem(C_hist_)
plt.subplot(122).set_title('Histograma da imagem original')

plt.figure(2)
plt.subplot(121), plt.imshow(img_out, 'gray')
plt.subplot(121).set_title('Imagem equalizada')
plt.subplot(122), plt.stem(C2_hist_)
plt.subplot(122).set_title('Histograma da imagem equalizada')

plt.show()
