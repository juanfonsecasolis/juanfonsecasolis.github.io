# ! python -m pip install lightkurve --upgrade
# https://lightkurve.github.io/lightkurve/quickstart.html
# https://docs.astropy.org/en/stable/index_getting_started.html
# pip install oktopus autograd

import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

# (in Flamsteed numbers)
corona_borealis_stars = [
    '8 CrB', # gamma 
    '7 CrB', # theta 
    '13 CrB' # Nusakan
    ]

for corona_borealis_star in corona_borealis_stars:
    lc = lk.search_lightcurve(corona_borealis_star, radius=3)[0].download()
    pandas_table = lc.to_pandas()
    #print(lc.time.flatten())
    # flux: electrons per second or energy per unit area and unit time (https://sites.astro.caltech.edu/~george/ay21/Fluxes%20and%20Magnitudes.pdf)
    
    # apparent_magnitude = -2.5 * np.log10(pandas_table['flux']) - 18.9822    # https://physics.stackexchange.com/a/395235 
    
    # https://github.com/lightkurve/lightkurve/discussions/1337
    # -2.5*np.log10(lc.flux.value/np.nanmedian(lc.flux.value))
    apparent_magnitude = -2.5 * np.log10(pandas_table['flux']/np.nanmedian(pandas_table['flux']))
    plt.plot(lc.time.to_value('decimalyear'), apparent_magnitude)

plt.legend(corona_borealis_stars)
plt.show()