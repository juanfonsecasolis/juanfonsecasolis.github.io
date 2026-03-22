#
# 2025 Juan M. Fonseca-Solis
#

import lightkurve as lk
import numpy as np

flamsteed_ursa_major = {
    'HR-5191': '85 Ursae Majoris',
    'HR-5054': '79 Ursae Majoris',
    'HR-4905': '77 Ursae Majoris',
    'HR-4660': '69 Ursae Majoris',
    'HR-4554': '64 Ursae Majoris',
    'HR-4295': '48 Ursae Majoris',
    'HR-4301': '50 Ursae Majoris',
    'HR-3757': '23 Ursae Majoris',
    'HR-3323': '1 Ursae Majoris',
    'HR-3888': '29 Ursae Majoris'
}

ursa_major_coordinates = {}

for starName in flamsteed_ursa_major:

    print(f'Downloading data for {starName}...')
    try:
        targetPixelFiles = lk.search_targetpixelfile(flamsteed_ursa_major[starName], 
            mission='TESS', limit=1)
        
        if 0<len(targetPixelFiles):
            targetPixelFile = targetPixelFiles[0].download()
            ra = targetPixelFile.ra
            dec = targetPixelFile.dec
            ursa_major_coordinates[starName] = { 'ra':ra, 'dec':dec }

    except Exception as e:
        print(f'Error while downloading data for {starName}. Skipping...\n')
        print(f'{repr(e)}\n')

print(ursa_major_coordinates)
print('Done.')