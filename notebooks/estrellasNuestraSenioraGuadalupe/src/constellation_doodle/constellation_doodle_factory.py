'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''
from constellation_doodle.constellation_doodle import ConstellationDoodle
from constellation_doodle.constellation_doodle_ursa_majoris import ConstellationDoodleUrsaMajoris

class ConstellationDoodleFactory():

    def __init__(self):
        pass

    def get_constellation_doodle(self, constellation_name:str) -> ConstellationDoodle:
        if(constellation_name=='osa_mayor'):
            return ConstellationDoodleUrsaMajoris()
        else:
            raise Exception(f'Unkown constellation {constellation_name}.')