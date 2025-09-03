#
# 2025 Juan M. Fonseca-Solis
#
# Referencias: 
# https://lightkurve.github.io/lightkurve/quickstart.html
# https://docs.astropy.org/en/stable/index_getting_started.html
# https://github.com/lightkurve/lightkurve/discussions/1337#discussioncomment-5866342
# https://lightkurve.github.io/lightkurve/reference/api/lightkurve.search_lightcurve.html?highlight=search_lightcurve
# https://spacetelescope.github.io/mast_notebooks/notebooks/Kepler/lightkurve_searching_for_data/lightkurve_searching_for_data.html#performing-a-cone-search

import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
from corona_borealis import flamsteed_CrB

fig, ax = plt.subplots()
for starName in flamsteed_CrB:

    print(f'Downloading data for {starName}...')

    try:
        light_curves = lk.search_lightcurve(flamsteed_CrB[starName], radius=0).download_all()

        for light_curve in [light_curves[0]]:

            days_of_the_year = [date.month*30+date.day for date in light_curve.time.to_value('datetime')]
            apparent_magnitude = light_curve.meta['TESSMAG'] + -2.5*np.log10(light_curve.flux.value/np.nanmedian(light_curve.flux.value)) 
            
            print(f'Type "days_of_the_year" = "{type(days_of_the_year)}"')
            print(f'Type "apparent_magnitude" = "{type(apparent_magnitude)}"')
            print('Plotting...')
            plt.plot(days_of_the_year, apparent_magnitude)

    except Exception as e:
        print(f'Error while downloading data for {starName}. Skipping...\n')
        print(f'{repr(e)}\n')

plt.legend(flamsteed_CrB.keys())
plt.ylabel('Apparent magnitude')
plt.xlabel('Day of the year')
plt.title('Corona Borealis')
plt.show()
print('Done.')