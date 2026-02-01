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

    def find_star_by_name(self, name:str) -> Star:
        return [x for x in self.stars if x.hr_name==name or x.common_name==name or x.flamsteed_name==name][0]

    def get_pairs(self, pair_names:list[list[str]]) -> list[list[Star]]:
        
        star_pairs = []
        for pair_name in pair_names:
            pair = [self.find_star_by_name(pair_name[0]), self.find_star_by_name(pair_name[1])]
            star_pairs.append(pair)

        return star_pairs