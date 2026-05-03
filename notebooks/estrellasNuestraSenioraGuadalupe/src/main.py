'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from astronomer import Astronomer
from constellation_factory import ConstellationFactory
import pprint
import numpy as np
import matplotlib.image as plt_img
import matplotlib.pyplot as plt
from coordinate_2d import Coordinate2D
from collections import OrderedDict

if __name__ == '__main__':

    # Planisferio de Stellarium 
    constellation_factory = ConstellationFactory(time=2280600.9895833335, 
        latitude=19.427778244018555, longitude=-99.1177749633789, altitude=0)
    constellation = constellation_factory.get_constellation('osa_mayor')
    constellation.print()
    constellation.plot()

    # Distancia entre las estrellas del planisferio
    star_pairs = constellation.get_pairs([
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
    dict_distances_planisphere_this_study = astronomer.calculate_distances_between_stair_pairs(star_pairs, astronomer.no_transform, None, None, None)
    #dict_distances_planisphere_this_study = astronomer.calculate_distances_between_stair_pairs(star_pairs, astronomer.mercator, 0, 0, 1)
    #dict_distances_planisphere_this_study = astronomer.calculate_distances_between_stair_pairs(star_pairs, astronomer.mercator, 99.133209 * np.pi/180.0, 19.432608 * np.pi/180.0, 6.37814 * 10**3)

    distances_planisphere_this_study = list(dict_distances_planisphere_this_study.values()) 
    pprint.pprint(dict_distances_planisphere_this_study)

    # Distancia entre las estrellas del manto
    HR_3757 = Coordinate2D('HR-3757', '23 Ursae Majoris', '23 UMa', 51.1+127.2, 421.1+181.6)
    HR_3323 = Coordinate2D('HR-3323', '01 Ursae Majoris', 'ο UMa', 50.7+127.2, 483.4+181.6)
    HR_4301 = Coordinate2D('HR-4301', '50 Ursae Majoris', 'Dubhe', 45.5+127.2, 343.0+181.6)
    HR_3888 = Coordinate2D('HR-3888', '29 Ursae Majoris', 'υ UMa', 94.8+127.2, 423.1+181.6)
    HR_4554 = Coordinate2D('HR-4554', '64 Ursae Majoris', 'Phecda', 111.6+127.2, 338.9+181.6)
    HR_4660 = Coordinate2D('HR-4660', '69 Ursae Majoris', 'Megrez', 77.6+127.2, 303.5+181.6)
    HR_4295 = Coordinate2D('HR-4295', '48 Ursae Majoris', 'Merak', 75.5+127.2, 373.4+181.6)
    HR_5191 = Coordinate2D('HR-5191', '85 Ursae Majoris', 'Alkaid', 62.9+127.2, 151.3+181.6)
    HR_5054 = Coordinate2D('HR-5054', '79 Ursae Majoris', 'Mizar', 42.2+127.2, 199.3+181.6) 
    HR_4905 = Coordinate2D('HR-4905', '77 Ursae Majoris', 'Alioth', 57.9+127.2, 243.6+181.6)

    stars = [HR_3757, HR_3323, HR_4301, HR_3888, HR_4554, HR_4660, HR_4295, HR_5191, HR_5054, HR_4905]
    asterism = [
        [HR_5191, HR_5054],
        [HR_5054, HR_4905],
        [HR_4905, HR_4660],
        [HR_4660, HR_4554],
        [HR_4554, HR_4295],
        [HR_4295, HR_4301],
        [HR_4301, HR_4660],
        [HR_4301, HR_3757],
        [HR_3757, HR_3323],
        [HR_3757, HR_3888]
    ]

    # plot stars
    plt.figure()
    img_original = plt_img.imread('../Virgen_de_guadalupe1.jpg')
    plt.imshow(img_original)
    for star in stars:
        plt.plot(star.x, star.y, 'x', color='white')
        plt.text(star.x+10.5, star.y-1.5, star.common_name, color='white')

    # zoom
    stars_x = [star.x for star in stars]
    stars_y = [star.y for star in stars]
    plt.xlim([min(stars_x)*0.9, max(stars_x)*1.1])
    plt.ylim([min(stars_y)*0.9, max(stars_y)*1.1])

    # plot asterisms and calculate the distances between pairs of stars
    dict_distances_tilma_this_study = OrderedDict()
    for (star1, star2) in asterism:
        plt.plot([star1.x, star2.x], [star1.y, star2.y], color='white')
        dict_distances_tilma_this_study[(star1.hr_name, star2.hr_name)] = float(np.sqrt(np.power(star2.x-star1.x,2)+np.power(star2.y-star1.y,2)))
    plt.show()

    pprint.pprint(dict_distances_tilma_this_study)
    distances_tilma_this_study = list(dict_distances_tilma_this_study.values())

    # Método de correlación de Pearson
    def pearson_correlation(x:list[float], y:list[float]) -> float:
        return 100.0 * np.cov(x,y, bias=True)[0][1]/(np.std(x)*np.std(y)) # 'bias=True' para normalizar por 1/N

    distances_tilma_ojeda = list(OrderedDict([
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
    ]).values())

    distances_planisphere_ojeda = list(OrderedDict([
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
    ]).values())

    correlation_tilma_ojeda_planisphere_ojeda = pearson_correlation(distances_tilma_ojeda, distances_planisphere_ojeda)
    correlation_tilma_ojeda_planisphere_this_study = pearson_correlation(distances_tilma_ojeda, distances_planisphere_this_study)
    correlation_tilma_planisphere_this_study  = pearson_correlation(distances_tilma_this_study, distances_planisphere_this_study)

    print(f'Correlaciones\n---')
    print(f'Tilma Ojeda / planisferio Ojeda: {correlation_tilma_ojeda_planisphere_ojeda:.2f}%')
    print(f'Tilma Ojeda / planisferio este estudio: {correlation_tilma_ojeda_planisphere_this_study:.2f}%')
    print(f'Tilma este estudio / planisferio este estudio: {correlation_tilma_planisphere_this_study:.2f}%')