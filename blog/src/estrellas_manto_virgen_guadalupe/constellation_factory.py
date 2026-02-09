'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from constellation import Constellation
from star import Star
from stellarium_dao import StellariumDao

class ConstellationFactory:

    def __init__(self, time:float, latitude:float, longitude:float, altitude:float):
        self.stellariumDao = StellariumDao()
        self.stellariumDao.setup_time(time)
        self.stellariumDao.setup_location(latitude, longitude, altitude)

    def fill_constellation_with_magnitude_and_ecuatorial_coordinates(self, constellation:Constellation):
        for star in constellation.stars:
            try:
                star.magnitude, star.ar_deg, star.dec_deg = self.stellariumDao.get_star_information(star.common_name)
            except Exception as e:
                print(f'{str(e)}\n')

    def get_constellation(self, constellation_name:str) -> Constellation:

        constellation = None
        if constellation_name=='ursa_majoris':

            list_of_stars = [
                Star('HR-5191', '85 Ursae Majoris', 'Alkaid'),
                Star('HR-5054', '79 Ursae Majoris', 'Mizar'), # Mizar A
                Star('HR-4905', '77 Ursae Majoris', 'Alioth'),
                Star('HR-4660', '69 Ursae Majoris', 'Megrez'),
                Star('HR-4554', '64 Ursae Majoris', 'Phecda'),
                Star('HR-4295', '48 Ursae Majoris', 'Merak'),
                Star('HR-4301', '50 Ursae Majoris', 'Dubhe'),
                Star('HR-3757', '23 Ursae Majoris', '23 UMa'),
                Star('HR-3323', '01 Ursae Majoris', 'ο UMa'),
                Star('HR-3888', '29 Ursae Majoris', 'υ UMa')
            ]
        
        else:
            raise Exception(f'Unknown constellation {constellation_name}.')
        
        constellation = Constellation(constellation_name, list_of_stars)
        self.fill_constellation_with_magnitude_and_ecuatorial_coordinates(constellation)
        return constellation