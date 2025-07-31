#
# 2025 Juan M. Fonseca-Solis
#
# Referencias: 
# https://lightkurve.github.io/lightkurve/quickstart.html
# https://docs.astropy.org/en/stable/index_getting_started.html
# https://github.com/lightkurve/lightkurve/discussions/1337#discussioncomment-5866342

import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
from corona_borealis import flamsteed_CrB

fig, ax = plt.subplots()
for starName in flamsteed_CrB:

    print(f'Downloading data for {starName}...')

    try:
        lc = lk.search_lightcurve(flamsteed_CrB[starName], radius=0)[0].download()
        apparent_magnitude = lc.meta['TESSMAG'] + -2.5*np.log10(lc.flux.value/np.nanmedian(lc.flux.value))
        print('Plotting...')
        days_of_the_year = [date.month*30+date.day for date in lc.time.to_value('datetime')]
        plt.plot(days_of_the_year, apparent_magnitude)

    except Exception as e:
        print(f'{repr(e)} error while downloading data for {starName}. Skipping...')

plt.legend(flamsteed_CrB.keys())
plt.ylabel('Apparent magnitude')
plt.xlabel('Day of the year')
plt.title('Corona Borealis')
plt.show()
print('Done.')