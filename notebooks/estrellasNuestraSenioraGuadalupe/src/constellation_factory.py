'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from constellation import Constellation
from star import Star
from stellarium_dao import StellariumDao
import numpy as np

class ConstellationFactory:

    def __init__(self, time:float, latitude:float, longitude:float, altitude:float):
        self.stellariumDao = StellariumDao()
        self.stellariumDao.setup_time(time)
        self.stellariumDao.setup_location(latitude, longitude, altitude)
        self.r = 1.0    # celestial spehere radius

    def fill_constellation_with_magnitude_and_coordinates(self, constellation:Constellation):
        for star in constellation.stars:
            try:
                star.magnitude, star.ar_deg, star.dec_deg = self.stellariumDao.get_star_information(star.common_name)
                star.x_cart = self.r * np.cos(np.pi * 0.5 - star.ar_rad)
                star.y_cart = self.r * np.cos(star.ar_rad)
                star.z_cart = self.r * np.sin(star.dec_rad)
            except Exception as e:
                print(f'{str(e)}\n')

    def ursa_majoris(self) -> (list[Star], list[list[Star]]):

        HR_5191 = Star('HR-5191', '85 Ursae Majoris', 'Alkaid')
        HR_5054 = Star('HR-5054', '79 Ursae Majoris', 'Mizar') # Mizar A
        HR_4905 = Star('HR-4905', '77 Ursae Majoris', 'Alioth')
        HR_4660 = Star('HR-4660', '69 Ursae Majoris', 'Megrez')
        HR_4554 = Star('HR-4554', '64 Ursae Majoris', 'Phecda')
        HR_4295 = Star('HR-4295', '48 Ursae Majoris', 'Merak')
        HR_4301 = Star('HR-4301', '50 Ursae Majoris', 'Dubhe')
        HR_3757 = Star('HR-3757', '23 Ursae Majoris', '23 UMa')
        HR_3323 = Star('HR-3323', '01 Ursae Majoris', 'ο UMa')
        HR_3888 = Star('HR-3888', '29 Ursae Majoris', 'υ UMa')

        stars = [HR_5191, HR_5054, HR_4905, HR_4660, HR_4554, HR_4295, HR_4301, HR_3757, HR_3323, HR_3888]
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

        return stars, asterism

    def cruz_del_sur(self) -> (list[Star], list[list[Star]]):

        HR_4763 = Star('HR-4763', 'gamma Cru', 'Gacrux')
        ANT_7 = Star('ANT 7', 'aplha Cru', 'Acrux')
        HR_4656 = Star('HR-4656', 'delta Cru', 'Imai')
        HR_4853 = Star('HR-4853', 'beta Cru', 'Mimosa')

        stars = [HR_4763, ANT_7, HR_4656, HR_4853]
        asterism = [
            [HR_4763, ANT_7],
            [HR_4656, HR_4853]
        ]

        return stars, asterism

    def get_constellation(self, constellation_name:str) -> Constellation:
        constellation = None
        if constellation_name == 'osa_mayor':
            stars, asterism = self.ursa_majoris() 
        elif constellation_name == 'cruz_del_sur':
            stars, asterism = self.cruz_del_sur()
        else:
            raise Exception(f'Unknown constellation "{constellation_name}".')
        
        constellation = Constellation(constellation_name, stars, asterism)
        self.fill_constellation_with_magnitude_and_coordinates(constellation)
        return constellation