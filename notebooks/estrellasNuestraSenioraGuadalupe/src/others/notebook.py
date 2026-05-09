'''
Refs.
1. https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html
'''
import sys
sys.path.append('../src/estrellas_manto_virgen_guadalupe')
from constellation_factory import ConstellationFactory
import numpy as np
import matplotlib.pylab as plt
from plot_sphere import plot_sphere

if __name__ == '__main__':

    # obtenemos la información de las estrellas de la constelación
    constellation_factory = ConstellationFactory(time=2280600.9895833335, 
        latitude=19.427778244018555, longitude=-99.1177749633789, altitude=0)
    
    constellation = constellation_factory.get_constellation('cruz_del_sur')
    #constellation = constellation_factory.get_constellation('osa_mayor')
    constellation.print()

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    r = 1    # radio terrestre

    plot_sphere(fig, ax, r)

    for star in constellation.stars:
        x = r * np.cos(np.pi * 0.5 - star.ar_rad)
        y = r * np.cos(star.ar_rad)
        z = r * np.sin(star.dec_rad)
        ax.scatter(x, y, z, color='red', marker='o')
    plt.show()
    