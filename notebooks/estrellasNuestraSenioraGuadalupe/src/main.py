'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from astronomer import Astronomer
from constellation_factory import ConstellationFactory
import pprint
from ojeda_measurements import OjedaMeasurements
from tilma_expert import TilmaExpert
from constellation_doodle.constellation_doodle_factory import ConstellationDoodleFactory
from statistics import pearson_correlation

def start(constellation_name: str):

    # Get planisphere from Stellarium 
    constellation_factory = ConstellationFactory(time=2280600.9895833335, 
        latitude=19.427778244018555, longitude=-99.1177749633789, altitude=0)
    constellation = constellation_factory.get_constellation(constellation_name)
    constellation.print()
    constellation.plot()

    # Get distance between stars in the planisphere
    astronomer = Astronomer()
    dict_distances_planisphere_this_study = astronomer.calculate_distances_between_stair_pairs(constellation.asterism, astronomer.no_transform, None, None, None)
    #dict_distances_planisphere_this_study = astronomer.calculate_distances_between_stair_pairs(constellation.asterism, astronomer.mercator, 0, 0, 1)
    #dict_distances_planisphere_this_study = astronomer.calculate_distances_between_stair_pairs(constellation.asterism, astronomer.mercator, 99.133209 * np.pi/180.0, 19.432608 * np.pi/180.0, 6.37814 * 10**3)

    distances_planisphere_this_study = list(dict_distances_planisphere_this_study.values()) 
    pprint.pprint(dict_distances_planisphere_this_study)

    # Draw stars in the tilma and calculate the distance between them
    tilma_expert = TilmaExpert('../img/Virgen_de_guadalupe1.jpg')
    constellation_doodle = ConstellationDoodleFactory().get_constellation_doodle(constellation_name)
    tilma_expert.plot_constellation(constellation_doodle)

    # plot asterisms and calculate the distances between pairs of stars
    dict_distances_tilma_this_study = tilma_expert.get_distances_between_stars(constellation_doodle)
    pprint.pprint(dict_distances_tilma_this_study)
    distances_tilma_this_study = list(dict_distances_tilma_this_study.values())

    # Apply the Pearson correlation method
    ojeda_measurements = OjedaMeasurements()
    distances_tilma_ojeda = list(ojeda_measurements.get_distances_tilma(constellation_name).values())
    distances_planisphere_ojeda = list(ojeda_measurements.get_distances_planisphere(constellation_name).values())

    correlation_tilma_ojeda_planisphere_ojeda = pearson_correlation(distances_tilma_ojeda, distances_planisphere_ojeda)
    correlation_tilma_ojeda_planisphere_this_study = pearson_correlation(distances_tilma_ojeda, distances_planisphere_this_study)
    correlation_tilma_planisphere_this_study  = pearson_correlation(distances_tilma_this_study, distances_planisphere_this_study)

    print(f'Correlaciones\n---')
    print(f'Tilma Ojeda / planisferio Ojeda: {correlation_tilma_ojeda_planisphere_ojeda:.2f}%')
    print(f'Tilma Ojeda / planisferio este estudio: {correlation_tilma_ojeda_planisphere_this_study:.2f}%')
    print(f'Tilma este estudio / planisferio este estudio: {correlation_tilma_planisphere_this_study:.2f}%')

if __name__ == '__main__':
    start('osa_mayor')