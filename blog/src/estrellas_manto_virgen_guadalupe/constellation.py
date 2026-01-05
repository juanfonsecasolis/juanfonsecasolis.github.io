''' 
 2025 Juan M. Fonseca-Solís
 Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''

from star import Star

class Constellation:

    def __init__(self, stars:list[Star]): 
        self.stars = stars

    def print(self):
        for star in self.stars:
            print(f'{star.common_name}, {star.hr_name}, {star.flamsteed_name}, mag: {star.magnitude:.2f}, ar: {star.ar}, dec: {star.dec}')
