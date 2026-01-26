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
        self.deg_to_rad_coeff = 2.0 * np.pi / 360.0
        self.rad_to_deg_coeff = 1.0 / self.deg_to_rad_coeff
        pass

    def find_kilometers_between_star_pair(self, star1:Star, star2:Star) -> float:
        '''
        Kilometers distance in the celestial sphere.
        '''
        
        dec1_rad = star1.dec * self.deg_to_rad_coeff
        ar1_rad = star1.ar * self.deg_to_rad_coeff

        dec2_rad = star2.dec * self.deg_to_rad_coeff
        ar2_rad = star2.ar * self.deg_to_rad_coeff

        d_rad = np.arccos(np.sin(dec1_rad) * np.sin(dec2_rad) + np.cos(dec1_rad) * np.cos(dec2_rad) * np.cos(ar1_rad-ar2_rad))
        return d_rad * self.rad_to_deg_coeff * 111.23

    def find_kilometers_between_star_pairs(self, pairs:list[list[Star]]) -> dict:

        distances = {}
        for [star1, star2] in pairs:
            d_km = self.find_kilometers_between_star_pair(star1, star2) if star1.dec is not None and star2.dec is not None else np.nan
            distances[(star1.hr_name, star2.hr_name)] = float(np.round(d_km, 2))
        return distances

    def computer_pearson_correlation(self, x:list[float], y:list[float]) -> float:
        return 100*np.cov(x,y, bias=True)[0][1]/(np.std(x)*np.std(y))