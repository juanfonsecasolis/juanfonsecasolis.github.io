'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

import matplotlib.pyplot as plt
import matplotlib.image as plt_img
import numpy as np

class Coordinate2D:
    
    def __init__(self, hr_name:str, flamsteed_name:str, common_name:str, x:float, y:float):
        self.hr_name = hr_name
        self.flamsteed_name = flamsteed_name
        self.common_name = common_name
        self.x = x
        self.y = y

HR_3757 = Coordinate2D('HR-3757', '23 Ursae Majoris', '23 UMa', 51.1, 421.1)
HR_3323 = Coordinate2D('HR-3323', '01 Ursae Majoris', 'ο UMa', 50.7, 483.4)
HR_4301 = Coordinate2D('HR-4301', '50 Ursae Majoris', 'Dubhe', 45.5, 343.0)
HR_3888 = Coordinate2D('HR-3888', '29 Ursae Majoris', 'υ UMa', 94.8, 423.1)
HR_4554 = Coordinate2D('HR-4554', '64 Ursae Majoris', 'Phecda', 111.6, 338.9)
HR_4660 = Coordinate2D('HR-4660', '69 Ursae Majoris', 'Megrez', 77.6, 303.5)
HR_4295 = Coordinate2D('HR-4295', '48 Ursae Majoris', 'Merak', 75.5, 373.4)
HR_5191 = Coordinate2D('HR-5191', '85 Ursae Majoris', 'Alkaid', 62.9, 151.3)
HR_5054 = Coordinate2D('HR-5054', '79 Ursae Majoris', 'Mizar', 42.2, 199.3) 
HR_4905 = Coordinate2D('HR-4905', '77 Ursae Majoris', 'Alioth', 57.9, 243.6)

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
img_original = plt_img.imread('../Virgen_de_guadalupe1_zoom.jpg')
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