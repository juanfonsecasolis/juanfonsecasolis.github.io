'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

import numpy as np
from collections import OrderedDict
from star import Star

class Astronomer:

    def __init__(self):
        pass

    def mercator(self, ar, dec, ar_0, dec_0, R):
        return R*(ar-ar_0), R*( np.log(np.tan(0.25*np.pi+0.5*dec)) - np.log(np.tan(0.25*np.pi+0.5*dec_0)) )

    def no_transform(self, ar, dec, ar_0, dec_0, R):
        return ar, dec

    def computer_pearson_correlation(self, x:list[float], y:list[float]) -> float:
        return 100*np.cov(x,y, bias=True)[0][1]/(np.std(x)*np.std(y))
    
    def calculate_distances_between_stair_pairs(self, constellation_pairs:list[list[Star]], func_transformacion, ar_0, dec_0, R) -> OrderedDict:
        km_per_degree = 111.23
        dict_distances_calc = OrderedDict()    # para preservar el orden de inserción empleamos un diccionario especial, en vez de {}
        for [star1, star2] in constellation_pairs:
            x_1, y_1 = func_transformacion(star1.ar_rad, star1.dec_rad, ar_0, dec_0, R)
            x_2, y_2 = func_transformacion(star2.ar_rad, star2.dec_rad, ar_0, dec_0, R)
            d_rad = np.arccos(np.sin(y_1) * np.sin(y_2) + np.cos(y_1) * np.cos(y_2) * np.cos(x_1-x_2))
            d_km = d_rad * 180.0/np.pi * km_per_degree
            dict_distances_calc[(star1.hr_name, star2.hr_name)] = float(np.round(d_km, 2))
        return dict_distances_calc