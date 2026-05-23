'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

from coordinate_2d import Coordinate2D
from tilma_expert_base import TilmaExpertBase
import matplotlib.image as plt_img
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np

class TilmaExpert(TilmaExpertBase):

    def __init__(self, tilma_image_path:str):
        super().__init__(tilma_image_path)
        self.HR_3323 = Coordinate2D('HR-3323', '01 Ursae Majoris', 'ο UMa', 177, 665)
        self.HR_3757 = Coordinate2D('HR-3757', '23 Ursae Majoris', '23 UMa', 177.4, 602.7)
        self.HR_4301 = Coordinate2D('HR-4301', '50 Ursae Majoris', 'Dubhe', 171.8, 524.6)
        self.HR_3888 = Coordinate2D('HR-3888', '29 Ursae Majoris', 'υ UMa', 221.1, 604.7)
        self.HR_4554 = Coordinate2D('HR-4554', '64 Ursae Majoris', 'Phecda', 237.9, 520.5)
        self.HR_4660 = Coordinate2D('HR-4660', '69 Ursae Majoris', 'Megrez', 203.9, 485.1)
        self.HR_4295 = Coordinate2D('HR-4295', '48 Ursae Majoris', 'Merak', 201.8, 555)
        self.HR_5191 = Coordinate2D('HR-5191', '85 Ursae Majoris', 'Alkaid', 189.2, 332.9)
        self.HR_5054 = Coordinate2D('HR-5054', '79 Ursae Majoris', 'Mizar', 168.5, 380.9) 
        self.HR_4905 = Coordinate2D('HR-4905', '77 Ursae Majoris', 'Alioth', 184.2, 425.2)

    def stars(self) -> list[Coordinate2D]:
        return [self.HR_3757, self.HR_3323, self.HR_4301, self.HR_3888, self.HR_4554, self.HR_4660, self.HR_4295, self.HR_5191, self.HR_5054, self.HR_4905]

    def asterism(self) -> list[list[Coordinate2D]]:
        return [
            [self.HR_5191, self.HR_5054],
            [self.HR_5054, self.HR_4905],
            [self.HR_4905, self.HR_4660],
            [self.HR_4660, self.HR_4554],
            [self.HR_4554, self.HR_4295],
            [self.HR_4295, self.HR_4301],
            [self.HR_4301, self.HR_4660],
            [self.HR_4301, self.HR_3757],
            [self.HR_3757, self.HR_3323],
            [self.HR_3757, self.HR_3888]
        ]
    
    def plot_constellation(self):
        # plot stars
        plt.figure()
        img_original = plt_img.imread('../img/Virgen_de_guadalupe1.jpg')
        plt.imshow(img_original)
        for star in self.stars():
            plt.plot(star.x, star.y, 'x', color='white')
            plt.text(star.x+10.5, star.y-1.5, star.common_name, color='white')

        # zoom
        stars_x = [star.x for star in self.stars()]
        stars_y = [star.y for star in self.stars()]
        plt.xlim([min(stars_x)*0.9, max(stars_x)*1.1])
        plt.ylim([max(stars_y)*1.1, min(stars_y)*0.9])

        # plot asterisms and calculate the distances between pairs of stars
        dict_distances_tilma_this_study = OrderedDict()
        for (star1, star2) in self.asterism():
            plt.plot([star1.x, star2.x], [star1.y, star2.y], color='white')
        plt.show()