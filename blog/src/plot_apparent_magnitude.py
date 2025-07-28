# 2025 Juan M. Fonseca-Solis
# ! python -m pip install lightkurve oktopus autograd
# https://lightkurve.github.io/lightkurve/quickstart.html
# https://docs.astropy.org/en/stable/index_getting_started.html

import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

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
        lc = lk.search_lightcurve(star, radius=0)[0].download()
        # https://github.com/lightkurve/lightkurve/discussions/1337#discussioncomment-5866342
        apparent_magnitude = lc.meta['TESSMAG'] + -2.5*np.log10(lc.flux.value/np.nanmedian(lc.flux.value))
        print('Plotting...')
        days_of_the_year = [date.month*30+date.day for date in lc.time.to_value('datetime')]
        plt.plot(days_of_the_year, apparent_magnitude)
    except Exception as e:
        print(f'{repr(e)} error while downloading data for {star}. Skipping...')

plt.legend(corona_borealis_constellation)
plt.ylabel('Apparent magnitude')
plt.xlabel('Day of the year')
#ax.tick_params(axis='x', labelrotation=45)
plt.show()
print('Done')