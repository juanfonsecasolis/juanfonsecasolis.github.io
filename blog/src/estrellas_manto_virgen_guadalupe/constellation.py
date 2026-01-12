'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from star import Star

class Constellation:

    def __init__(self, name, stars:list[Star]): 
        self.name = name
        self.stars = stars

    def print(self):
        print(f'Constellation "{self.name}":')
        print('-----------')
        for star in self.stars:
            star.print()
