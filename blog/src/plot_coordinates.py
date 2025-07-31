#
# 2025 Juan M. Fonseca-Solis
#
# Referencias: 
# https://lightkurve.github.io/lightkurve/tutorials/1-getting-started/using-target-pixel-file-products.html?highlight=skycoord
# https://en.wikipedia.org/wiki/List_of_stars_in_Corona_Borealis

import lightkurve as lk
import matplotlib.pyplot as plt
from corona_borealis import flamsteed_CrB

fig, ax = plt.subplots()
for starName in flamsteed_CrB:

    print(f'Downloading data for {starName}...')
    try:
        targetPixelFile = lk.search_targetpixelfile(flamsteed_CrB[starName], radius=0)[0].download()
        print('Plotting...')
        cartesian_coordinates = targetPixelFile.wcs.pixel_to_world(0, 0).cartesian
        plt.scatter(cartesian_coordinates.x, cartesian_coordinates.y)
    except Exception as e:
        print(f'"{repr(e)}" error while downloading data for {starName}. Skipping...')

plt.legend(flamsteed_CrB.keys())
plt.ylabel('Y')
plt.xlabel('X')
plt.title('Corona Borealis')
plt.show()
print('Done.')