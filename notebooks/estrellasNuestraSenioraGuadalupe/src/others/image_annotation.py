'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

import sys
sys.path.append('../')
import matplotlib.pyplot as plt
import matplotlib.image as plt_img
from constellation_doodle.coordinate_2d import Coordinate2D
import numpy as np

HR_3323 = Coordinate2D('HR-3323', '01 Ursae Majoris', 'ο UMa', 50.7+126.3, 483.4+181.6)
HR_3757 = Coordinate2D('HR-3757', '23 Ursae Majoris', '23 UMa', 51.1+126.3, 421.1+181.6)
HR_4301 = Coordinate2D('HR-4301', '50 Ursae Majoris', 'Dubhe', 45.5+126.3, 343.0+181.6)
HR_3888 = Coordinate2D('HR-3888', '29 Ursae Majoris', 'υ UMa', 94.8+126.3, 423.1+181.6)
HR_4554 = Coordinate2D('HR-4554', '64 Ursae Majoris', 'Phecda', 111.6+126.3, 338.9+181.6)
HR_4660 = Coordinate2D('HR-4660', '69 Ursae Majoris', 'Megrez', 77.6+126.3, 303.5+181.6)
HR_4295 = Coordinate2D('HR-4295', '48 Ursae Majoris', 'Merak', 75.5+126.3, 373.4+181.6)
HR_5191 = Coordinate2D('HR-5191', '85 Ursae Majoris', 'Alkaid', 62.9+126.3, 151.3+181.6)
HR_5054 = Coordinate2D('HR-5054', '79 Ursae Majoris', 'Mizar', 42.2+126.3, 199.3+181.6) 
HR_4905 = Coordinate2D('HR-4905', '77 Ursae Majoris', 'Alioth', 57.9+126.3, 243.6+181.6)

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

stars = [HR_3757, HR_3323, HR_4301, HR_3888, HR_4554, HR_4660, HR_4295, HR_5191, HR_5054, HR_4905]

plt.figure()
img_original = plt_img.imread('../../img/Virgen_de_guadalupe1.jpg')
plt.imshow(img_original)

for star in stars:
    plt.plot(star.x, star.y, 'x', color='white')
    plt.text(star.x+10.5, star.y-1.5, star.common_name, color='white')

distances = {}
for (star1, star2) in asterism:
    plt.plot([star1.x, star2.x], [star1.y, star2.y], color='white')
    distances[star1.hr_name] = float(np.sqrt(np.power(star2.x-star1.x,2)+np.power(star2.y-star1.y,2)))

plt.show()
print(distances)