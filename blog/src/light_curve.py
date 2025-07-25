# 2025 Juan M. Fonseca-Solis
# ! python -m pip install lightkurve oktopus autograd
# https://lightkurve.github.io/lightkurve/quickstart.html
# https://docs.astropy.org/en/stable/index_getting_started.html

import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

# Using Flamsteed format.
corona_borealis_stars = [
    '8 CrB', # gamma 
    '7 CrB', # theta 
    '13 CrB' # Nusakan
    ]

fig, ax = plt.subplots()
for corona_borealis_star in corona_borealis_stars:

    print(f'Downloading data for {corona_borealis_star}...')
    lc = lk.search_lightcurve(corona_borealis_star, radius=3)[0].download()

    # https://github.com/lightkurve/lightkurve/discussions/1337#discussioncomment-5866342
    apparent_magnitude = lc.meta['TESSMAG'] + -2.5*np.log10(lc.flux.value/np.nanmedian(lc.flux.value))

    print('Plotting...')
    plt.plot(lc.time.to_value('datetime'), apparent_magnitude)

plt.legend(corona_borealis_stars)
plt.ylabel('Apparent magnitude')
plt.xlabel('Time')
ax.tick_params(axis='x', labelrotation=45)
plt.show()
print('Done')