'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from astronomer import Astronomer
from constellation_factory import ConstellationFactory
import pprint

if __name__ == '__main__':

    constellation_factory = ConstellationFactory(time=2280600.9895833335, latitude=19.427778244018555, longitude=-99.1177749633789, altitude=0)
    ursa_majoris_constellation = constellation_factory.get_constellation('ursa_majoris')
    ursa_hr_pairs = ursa_majoris_constellation.get_pairs([
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
    ])

    astronomer = Astronomer()
    ds_sky = astronomer.find_kilometers_between_star_pairs(ursa_hr_pairs)
    print(f'\nKilometers between stars (celestial sphere model):\n-----------')
    pprint.pprint(ds_sky)