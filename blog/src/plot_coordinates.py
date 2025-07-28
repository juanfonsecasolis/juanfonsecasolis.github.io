# 2025 Juan M. Fonseca-Solis
# ! python -m pip install lightkurve oktopus autograd
# https://lightkurve.github.io/lightkurve/tutorials/1-getting-started/using-target-pixel-file-products.html?highlight=skycoord
# https://en.wikipedia.org/wiki/List_of_stars_in_Corona_Borealis

import lightkurve as lk
import matplotlib.pyplot as plt

# Using Flamsteed format.
corona_borealis_constellation = [
    '3 CrB', # beta
    '5 CrB', # alpha
    '4 CrB', # theta
    '8 CrB', # gamma
    '10 CrB', # delta 
    '13 CrB', # epsilon (Nusakan)
    '14 CrB' # iota
    ]

fig, ax = plt.subplots()
for star in corona_borealis_constellation:

    print(f'Downloading data for {star}...')
    try:
        targetPixelFile = lk.search_targetpixelfile(star, radius=0)[0].download()
        print('Plotting...')
        cartesian_coordinates = targetPixelFile.wcs.pixel_to_world(0, 0).cartesian
        plt.scatter(cartesian_coordinates.x, cartesian_coordinates.y)
    except Exception as e:
        print(f'"{repr(e)}" error while downloading data for {star}. Skipping...')

plt.legend(corona_borealis_constellation)
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
print('Done')