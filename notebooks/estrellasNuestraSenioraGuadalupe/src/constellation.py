'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from star import Star
import matplotlib.pylab as plt

class Constellation:

    def __init__(self, name:str, stars:list[Star], asterism:list[list[Star]]): 
        self.name = name
        self.stars = stars
        self.asterism = asterism

    def print(self):
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
    
    def plot(self) -> None:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        
        # draw stars
        for star in self.stars:
            ax.scatter(star.x_cart, star.y_cart, star.z_cart, marker='o')

        # draw asterism
        for(star1, star2) in self.asterism:
            ax.plot([star1.x_cart, star2.x_cart], [star1.y_cart, star2.y_cart], [star1.z_cart, star2.z_cart], color='b')

        plt.legend([f'{x.hr_name} - {x.common_name}' for x in self.stars], loc=(1.1, 0.25))
        plt.show()