'''
2025-2026 Juan M. Fonseca-Solís
Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''

from star import Star
from constellation import Constellation
from astronomer import Astronomer
from constellation_factory import ConstellationFactory
import pprint

if __name__ == '__main__':

    ursa_hr_pairs = [
        ['HR-5191', 'HR-5054'],
        ['HR-5054', 'HR-4905'],
        ['HR-4905', 'HR-4660'],
        ['HR-4660', 'HR-4554'],
        ['HR-4554', 'HR-4295'],
        ['HR-4295', 'HR-4301'],
        ['HR-4301', 'HR-4660'],
        ['HR-4301', 'HR-3757'],
        ['HR-3757', 'HR-3323'],
        ['HR-3757', 'HR-3888']
    ]
    
    constellation_factory = ConstellationFactory()
    ursa_majoris_constellation = constellation_factory.get_constellation('ursa_majoris')

    astronomer = Astronomer()
    ds_sky = astronomer.find_kilometers_between_star_pairs(ursa_hr_pairs)
    pprint.pprint(ds_sky)

    
