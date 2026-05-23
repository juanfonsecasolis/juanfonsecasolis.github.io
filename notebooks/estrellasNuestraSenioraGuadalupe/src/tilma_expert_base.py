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
from coordinate_2d import Coordinate2D
from abc import ABC, abstractmethod
from collections import OrderedDict

class TilmaExpertBase(ABC):

    def __init__(self, tilma_image_path):
        self.tilma_image_path = tilma_image_path

    @abstractmethod
    def stars(self) -> list[Coordinate2D]:
        pass

    @abstractmethod
    def asterism(self) -> list[list[Coordinate2D]]:
        pass

    def get_distances_between_stars(self) -> dict:
        dict_distances = OrderedDict()
        for (star1, star2) in self.asterism():
            plt.plot([star1.x, star2.x], [star1.y, star2.y], color='white')
            dict_distances[(star1.hr_name, star2.hr_name)] = float(np.sqrt(np.power(star2.x-star1.x,2)+np.power(star2.y-star1.y,2)))
        return dict_distances

    def plot(self) -> None:
        fig = plt.figure()
        img_original = plt_img.imread(self.tilma_image_path)
        plt.imshow(img_original)

        # plot stars
        for star in self.stars():
            plt.plot(star.x, star.y, 'x', color='white')
            plt.text(star.x+10.5, star.y-1.5, star.common_name, color='white')

        # plot asterim
        for (star1, star2) in self.asterism():
            plt.plot([star1.x, star2.x], [star1.y, star2.y], color='white')

        # zoom
        stars_x = [star.x for star in self.stars()]
        stars_y = [star.y for star in self.stars()]
        plt.xlim([min(stars_x)*0.9, max(stars_x)*1.3])
        plt.ylim([max(stars_y)*1.1, min(stars_y)*0.9])  # reverse order to avoid rotation
        
        plt.show()