'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

import numpy as np
from constellation import Constellation
from star import Star

class Astronomer:

    def __init__(self):
        pass

    def find_celestial_sphere_kilometers_between_stars(self, star1:Star, star2:Star) -> float: 
        d_rad = np.arccos(np.sin(star1.dec_rad) * np.sin(star2.dec_rad) + np.cos(star1.dec_rad) * np.cos(star2.dec_rad) * np.cos(star1.ar_rad-star2.ar_rad))
        rad_to_dec_coeff = 360.0/(2.0 * np.pi)
        return d_rad * rad_to_dec_coeff * 111.23

    def find_kilometers_between_star_pairs(self, pairs:list[list[Star]]) -> dict:

        distances = {} 
        for [star1, star2] in pairs:
            d_km = self.find_celestial_sphere_kilometers_between_stars(star1, star2) 
            distances[(star1.hr_name, star2.hr_name)] = float(np.round(d_km, 2))
        return distances

    def computer_pearson_correlation(self, x:list[float], y:list[float]) -> float:
        return 100*np.cov(x,y, bias=True)[0][1]/(np.std(x)*np.std(y))