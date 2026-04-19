'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

import matplotlib.pyplot as plt
import matplotlib.image as plt_img 
from scipy import ndimage, datasets
import numpy as np

from skimage.filters import unsharp_mask

fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side

img_original = plt_img.imread('../Virgen_de_guadalupe1_zoom.jpg')
#img_original = plt_img.imread('../jfonseca.IMG_20260103_190110_zoom.jpg')
#img_original = plt_img.imread('../jfonseca.IMG_20260103_190110_zoom.jpg')[:, :, 0]  # to gray scale

# laplace
#img_filtered = ndimage.laplace(img_original)

# laplace & gaussian
#img_filtered = ndimage.gaussian_laplace(img_original, sigma=3)

# sobel
#img_original = img_original.astype('int32')
#sobel_h = ndimage.sobel(img_original, 0)  # horizontal gradient
#sobel_v = ndimage.sobel(img_original, 1)  # vertical gradient
#magnitude = np.sqrt(sobel_h**2 + sobel_v**2)
#magnitude *= 255.0 / np.max(magnitude)  # normalization
#img_filtered = magnitude

# scikit
img_filtered = unsharp_mask(img_original, radius=1, amount=1)

# ToDo: 
# https://scipy-lectures.org/advanced/image_processing/auto_examples/plot_sharpen.html
# https://scikit-image.org/docs/stable/auto_examples/filters/plot_unsharp_mask.html

ax1.imshow(img_original)
ax2.imshow(img_filtered)
plt.show()