'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

import matplotlib.pyplot as plt
import matplotlib.image as plt_img  

img = plt_img.imread('../jfonseca.IMG_20260103_190110.jpg')
imgplot = plt.imshow(img)
plt.plot(214.3, 748.1, marker='.', color='white')
plt.show()