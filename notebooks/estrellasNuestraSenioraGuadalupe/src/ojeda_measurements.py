'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  * 2025-2026 Juan M. Fonseca-Solís. Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre de 1531 a las 6:45 am en la ciudad de México.
'''
from collections import OrderedDict

class OjedaMeasurements():

    def __init__(self):
        pass
        
    def get_distances_tilma(self, constellation_name:str) -> OrderedDict:
        if(constellation_name=='osa_mayor'):
            return OrderedDict([
                (('HR-5191', 'HR-5054'), 650.0),
                (('HR-5054', 'HR-4905'), 550.0),
                (('HR-4905', 'HR-4660'), 650.0),
                (('HR-4660', 'HR-4554'), 650.0),
                (('HR-4554', 'HR-4295'), 700.0),
                (('HR-4295', 'HR-4301'), 600.0),
                (('HR-4301', 'HR-4660'), 800.0),
                (('HR-4301', 'HR-3757'), 950.0),
                (('HR-3757', 'HR-3323'), 800.0),
                (('HR-3757', 'HR-3888'), 600.0)
            ])
        else:
            raise Exception(f'Unknown constellation "{self.constellation_name}".')
        
    def get_distances_planisphere(self, constellation_name:str) -> OrderedDict:
        if(constellation_name=='osa_mayor'):
            return OrderedDict([
                (('HR-5191', 'HR-5054'), 744.16),
                (('HR-5054', 'HR-4905'), 484.98),
                (('HR-4905', 'HR-4660'), 604.01),
                (('HR-4660', 'HR-4554'), 503.89),
                (('HR-4554', 'HR-4295'), 878.76),
                (('HR-4295', 'HR-4301'), 598.44),
                (('HR-4301', 'HR-4660'), 1134.6),
                (('HR-4301', 'HR-3757'), 1193.55),
                (('HR-3757', 'HR-3323'), 837.6),
                (('HR-3757', 'HR-3888'), 518.35)
            ])
        else:
            raise Exception(f'Unknown constellation "{self.constellation_name}".')
            