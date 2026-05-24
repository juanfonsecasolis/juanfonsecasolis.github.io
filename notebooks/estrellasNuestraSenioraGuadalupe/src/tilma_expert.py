'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

import matplotlib.image as plt_img
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np
from constellation_doodle.constellation_doodle import ConstellationDoodle

class TilmaExpert():

    def __init__(self, tilma_image_path:str):
        self.tilma_image_path = tilma_image_path
    
    def plot_constellation(self, constellation_doodle:ConstellationDoodle):
        # plot stars
        plt.figure()
        img_original = plt_img.imread(self.tilma_image_path)
        plt.imshow(img_original)
        for star in constellation_doodle.stars:
            plt.plot(star.x, star.y, 'x', color='white')
            plt.text(star.x+10.5, star.y-1.5, star.common_name, color='white')

        # zoom
        stars_x = [star.x for star in constellation_doodle.stars]
        stars_y = [star.y for star in constellation_doodle.stars]
        plt.xlim([min(stars_x)*0.9, max(stars_x)*1.1])
        plt.ylim([max(stars_y)*1.1, min(stars_y)*0.9])  # reverse order to avoid rotation

        # plot asterisms and calculate the distances between pairs of stars
        for (star1, star2) in constellation_doodle.asterism:
            plt.plot([star1.x, star2.x], [star1.y, star2.y], color='white')
        plt.show()

    def get_distances_between_stars(self, constellation_doodle:ConstellationDoodle) -> dict:
        dict_distances = OrderedDict()
        for (star1, star2) in constellation_doodle.asterism:
            plt.plot([star1.x, star2.x], [star1.y, star2.y], color='white')
            dict_distances[(star1.hr_name, star2.hr_name)] = float(np.sqrt(np.power(star2.x-star1.x,2)+np.power(star2.y-star1.y,2)))
        return dict_distances