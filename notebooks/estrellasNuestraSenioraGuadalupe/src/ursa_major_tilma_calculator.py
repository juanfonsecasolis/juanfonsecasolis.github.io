'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.

  References:
  - https://stackoverflow.com/a/35287898  
'''

from coordinate_2d import Coordinate2D
from tilma_calculator_base import TilmaCalculatorBase

class UrsaMajorTilmaCalculator(TilmaCalculatorBase):

    def __init__(self, tilma_image_path:str):
        super().__init__(tilma_image_path)
        self.HR_3757 = Coordinate2D('HR-3757', '23 Ursae Majoris', '23 UMa', 51.1+127.2, 421.1+181.6)
        self.HR_3323 = Coordinate2D('HR-3323', '01 Ursae Majoris', 'ο UMa', 50.7+127.2, 483.4+181.6)
        self.HR_4301 = Coordinate2D('HR-4301', '50 Ursae Majoris', 'Dubhe', 45.5+127.2, 343.0+181.6)
        self.HR_3888 = Coordinate2D('HR-3888', '29 Ursae Majoris', 'υ UMa', 94.8+127.2, 423.1+181.6)
        self.HR_4554 = Coordinate2D('HR-4554', '64 Ursae Majoris', 'Phecda', 111.6+127.2, 338.9+181.6)
        self.HR_4660 = Coordinate2D('HR-4660', '69 Ursae Majoris', 'Megrez', 77.6+127.2, 303.5+181.6)
        self.HR_4295 = Coordinate2D('HR-4295', '48 Ursae Majoris', 'Merak', 75.5+127.2, 373.4+181.6)
        self.HR_5191 = Coordinate2D('HR-5191', '85 Ursae Majoris', 'Alkaid', 62.9+127.2, 151.3+181.6)
        self.HR_5054 = Coordinate2D('HR-5054', '79 Ursae Majoris', 'Mizar', 42.2+127.2, 199.3+181.6) 
        self.HR_4905 = Coordinate2D('HR-4905', '77 Ursae Majoris', 'Alioth', 57.9+127.2, 243.6+181.6)

    def stars(self) -> list[Coordinate2D]:
        return [self.HR_3757, self.HR_3323, self.HR_4301, self.HR_3888, self.HR_4554, self.HR_4660, self.HR_4295, self.HR_5191, self.HR_5054, self.HR_4905]

    def asterism(self) -> list[list[Coordinate2D]]:
        return [
            [self.HR_5191, self.HR_5054],
            [self.HR_5054, self.HR_4905],
            [self.HR_4905, self.HR_4660],
            [self.HR_4660, self.HR_4554],
            [self.HR_4554, self.HR_4295],
            [self.HR_4295, self.HR_4301],
            [self.HR_4301, self.HR_4660],
            [self.HR_4301, self.HR_3757],
            [self.HR_3757, self.HR_3323],
            [self.HR_3757, self.HR_3888]
        ]