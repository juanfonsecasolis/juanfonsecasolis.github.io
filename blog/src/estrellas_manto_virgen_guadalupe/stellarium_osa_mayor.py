'''
2025-2026 Juan M. Fonseca-Solís
Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''

import numpy as np
from star import Star
from constellation import Constellation
import pprint
from stellarium_dao import StellariumDao 

def decimal_to_degrees_minutes_seconds(x:float) -> list:
    degrees = int(x)
    minutes = (x-degrees)*60.0
    seconds = (minutes-int(minutes))*60.0
    return int(degrees), int(minutes), round(seconds, 1)

def print_ar_dec(ar, dec):
    ar_hours, ar_minutes, ar_seconds = decimal_to_degrees_minutes_seconds(ar)
    dec_hours, dec_minutes, dec_seconds = decimal_to_degrees_minutes_seconds(dec)
    ar_str = f'{ar} ({ar_hours}h {ar_minutes}m {ar_seconds}s)'
    dec_str = f'{dec} ({dec_hours}° {dec_minutes}m {dec_seconds}s)'
    print(f'AR/Dec (en fecha): {ar_str} / {dec_str}\n') 

def fill_with_magnitude_and_ecuatorial_coordinates(constellation:Constellation):

    for star in constellation.stars:
        try:
            star.magnitude, star.ar, star.dec = get_star_information(star.common_name)
        except Exception as e:
            print(f'{str(e)}\n')

def find_first_star_that_matches_hr_name(constellation:Constellation, hr_name:str):
    results = [x for x in constellation.stars if x.hr_name==hr_name]
    return None if results is None else results[0]

def compute_kilometer_distance_between_stars(star1:Star, star2:Star) -> float:
    '''
    Kilometers distance in the celestial sphere.
    '''
    deg_to_rad_coeff = 2.0 * np.pi / 360.0
    rad_to_deg_coeff = 1.0 / deg_to_rad_coeff

    dec1_rad = star1.dec * deg_to_rad_coeff
    ar1_rad = star1.ar * deg_to_rad_coeff

    dec2_rad = star2.dec * deg_to_rad_coeff
    ar2_rad = star2.ar * deg_to_rad_coeff

    d_rad = np.arccos(np.sin(dec1_rad)*np.sin(dec2_rad) + np.cos(dec1_rad)*np.cos(dec2_rad)*np.cos(ar1_rad-ar2_rad))
    return d_rad * rad_to_deg_coeff * 111.23

def find_kilometer_distance_between_pairs(pairs:list[list[str]]) -> dict:
    distances = {}
    for pair in pairs:
        star1 = find_first_star_that_matches_hr_name(ursa_constellation, pair[0])
        star2 = find_first_star_that_matches_hr_name(ursa_constellation, pair[1])
        d_km = compute_kilometer_distance_between_stars(star1, star2) if star1.dec is not None and star2.dec is not None else np.nan
        #distances[(star1, star2)] = np.round(d_km, 2)
        distances[(pair[0], pair[1])] = np.round(d_km, 2)
        #print(f'{star1.hr_name} ({star1.common_name}) a {star2.hr_name} ({star2.common_name}): {d_km:.2f} km.')
    return distances

def computer_pearson_correlation(x:list[float], y:list[float]) -> float:
    return 100*np.cov(x,y, bias=True)[0][1]/(np.std(x)*np.std(y))

if __name__ == '__main__':

    ursa_constellation = Constellation([
        Star('HR-5191', '85 Ursae Majoris', 'Alkaid'),
        Star('HR-5054', '79 Ursae Majoris', 'Mizar'), # Mizar A
        Star('HR-4905', '77 Ursae Majoris', 'Alioth'),
        Star('HR-4660', '69 Ursae Majoris', 'Megrez'),
        Star('HR-4554', '64 Ursae Majoris', 'Phecda'),
        Star('HR-4295', '48 Ursae Majoris', 'Merak'),
        Star('HR-4301', '50 Ursae Majoris', 'Dubhe'),
        Star('HR-3757', '23 Ursae Majoris', '23 UMa'),
        Star('HR-3323', '01 Ursae Majoris', 'ο UMa'),
        Star('HR-3888', '29 Ursae Majoris', 'υ UMa')
    ])
    
    ursa_hr_pairs = [
        ['HR-5191', 'HR-5054'],
        ['HR-5054', 'HR-4905'],
        ['HR-4905', 'HR-4660'],
        ['HR-4660', 'HR-4554'],
        ['HR-4554', 'HR-4295'],
        ['HR-4295', 'HR-4301'],
        ['HR-4301', 'HR-4660'],
        ['HR-4301', 'HR-3757'],
        ['HR-3757', 'HR-3323'],
        ['HR-3757', 'HR-3888']
    ]
    
    stellariumDao = StellariumDao()
    stellariumDao.setup_time(time=2280600.9895833335)
    stellariumDao.setup_location(latitude=19.427778244018555, longitude=-99.1177749633789, altitude=0)

    fill_with_magnitude_and_ecuatorial_coordinates(ursa_constellation)
    ds_sky = find_kilometer_distance_between_pairs(ursa_hr_pairs)
    pprint.pprint(ds_sky)

    
