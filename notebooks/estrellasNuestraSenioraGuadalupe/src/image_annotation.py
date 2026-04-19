'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

import matplotlib.pyplot as plt
import matplotlib.image as plt_img 

class Coordinate2D:
    
    def __init__(self, hr_name:str, flamsteed_name:str, common_name:str, x:float, y:float):
        self.hr_name = hr_name
        self.flamsteed_name = flamsteed_name
        self.common_name = common_name
        self.x = x
        self.y = y
        
'''
HR_5191 = Coordinate2D('HR-5191', '85 Ursae Majoris', 'Alkaid')
HR_5054 = Coordinate2D('HR-5054', '79 Ursae Majoris', 'Mizar') 
HR_4905 = Coordinate2D('HR-4905', '77 Ursae Majoris', 'Alioth')
HR_4660 = Coordinate2D('HR-4660', '69 Ursae Majoris', 'Megrez')
HR_4554 = Coordinate2D('HR-4554', '64 Ursae Majoris', 'Phecda')
HR_4295 = Coordinate2D('HR-4295', '48 Ursae Majoris', 'Merak')
HR_4301 = Coordinate2D('HR-4301', '50 Ursae Majoris', 'Dubhe')
HR_3757 = Coordinate2D('HR-3757', '23 Ursae Majoris', '23 UMa', 215, 680)
HR_3323 = Coordinate2D('HR-3323', '01 Ursae Majoris', 'ο UMa', 214.3, 748.1)
HR_3888 = Coordinate2D('HR-3888', '29 Ursae Majoris', 'υ UMa')

stars = [HR_5191, HR_5054, HR_4905, HR_4660, HR_4554, HR_4295, HR_4301, HR_3757, HR_3323, HR_3888]
asterism = [
    [HR_5191, HR_5054],
    [HR_5054, HR_4905],
    [HR_4905, HR_4660],
    [HR_4660, HR_4554],
    [HR_4554, HR_4295],
    [HR_4295, HR_4301],
    [HR_4301, HR_4660],
    [HR_4301, HR_3757],
    [HR_3757, HR_3323],
    [HR_3757, HR_3888],
    [HR_3888, HR_3323]]
'''

from scipy import ndimage, datasets
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side
img_original = plt_img.imread('../jfonseca.IMG_20260103_190110_zoom.jpg')[:, :, 0]  # to gray scale

# laplace
#img_filtered = ndimage.laplace(img_original)

# laplace & gaussian
img_filtered = ndimage.gaussian_laplace(img_original, sigma=3)

# sobel
#img_original = img_original.astype('int32')
#sobel_h = ndimage.sobel(img_original, 0)  # horizontal gradient
#sobel_v = ndimage.sobel(img_original, 1)  # vertical gradient
#magnitude = np.sqrt(sobel_h**2 + sobel_v**2)
#magnitude *= 255.0 / np.max(magnitude)  # normalization
#img_filtered = magnitude

# ToDo: 
# https://scipy-lectures.org/advanced/image_processing/auto_examples/plot_sharpen.html
# https://scikit-image.org/docs/0.25.x/auto_examples/filters/plot_unsharp_mask.html

ax1.imshow(img_original)
ax2.imshow(img_filtered)
plt.show()