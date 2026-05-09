'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''
from tilma_calculator_base import TilmaCalculatorBase
from ursa_major_tilma_calculator import UrsaMajorTilmaCalculator

class TilmaCalculatorFactory():

    def __init__(self, tilma_image_path:str):
        self.tilma_image_path = tilma_image_path
        pass

    def get_tilma_calculator(self, constellation_name:str) -> TilmaCalculatorBase:
        if(constellation_name=='osa_mayor'):
            return UrsaMajorTilmaCalculator(self.tilma_image_path)
        else:
            raise Exception(f'Unkown constellation {constellation_name}.')