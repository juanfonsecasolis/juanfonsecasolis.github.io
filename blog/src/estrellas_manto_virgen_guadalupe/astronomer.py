'''
2025-2026 Juan M. Fonseca-Solís
Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''
import numpy as np
from constellation import Constellation
from star import Star

class Astronomer:

    def __init__(self):
        pass

    def find_first_star_that_matches_hr_name(self, constellation:Constellation, hr_name:str):
        results = [x for x in constellation.stars if x.hr_name==hr_name]
        return None if results is None else results[0]

    def find_kilometers_between_star_pairs(self, star1:Star, star2:Star) -> float:
        '''
        Kilometers distance in the celestial sphere.
        '''
        deg_to_rad_coeff = 2.0 * np.pi / 360.0
        rad_to_deg_coeff = 1.0 / deg_to_rad_coeff

        dec1_rad = star1.dec * deg_to_rad_coeff
        ar1_rad = star1.ar * deg_to_rad_coeff

        dec2_rad = star2.dec * deg_to_rad_coeff
        ar2_rad = star2.ar * deg_to_rad_coeff

        d_rad = np.arccos(np.sin(dec1_rad)*np.sin(dec2_rad) + np.cos(dec1_rad)*np.cos(dec2_rad)*np.cos(ar1_rad-ar2_rad))
        return d_rad * rad_to_deg_coeff * 111.23

    def find_kilometers_between_star_pairs(self, pairs:list[list[str]], constellation:Constellation) -> dict:
        distances = {}

        for pair in pairs:
            star1 = self.find_first_star_that_matches_hr_name(constellation, pair[0])
            star2 = self.find_first_star_that_matches_hr_name(constellation, pair[1])
            d_km = self.find_kilometers_between_star_pairs(star1, star2) if star1.dec is not None and star2.dec is not None else np.nan
            distances[(pair[0], pair[1])] = np.round(d_km, 2)

        return distances

    def computer_pearson_correlation(self, x:list[float], y:list[float]) -> float:
        return 100*np.cov(x,y, bias=True)[0][1]/(np.std(x)*np.std(y))