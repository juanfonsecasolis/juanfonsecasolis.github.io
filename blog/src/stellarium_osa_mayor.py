'''
2025 Juan M. Fonseca-Solís
Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''

import requests
import numpy as np
from star_coordinate import StarCoordinate

ursa_major_mapping = [
    StarCoordinate('HR-5191', '85 Ursae Majoris', 'Alkaid'),
    StarCoordinate('HR-5054', '79 Ursae Majoris', 'Mizar A'),
    StarCoordinate('HR-4905', '77 Ursae Majoris', 'Alioth'),
    StarCoordinate('HR-4660', '69 Ursae Majoris', 'Megrez'),
    StarCoordinate('HR-4554', '64 Ursae Majoris', 'Phecda'),
    StarCoordinate('HR-4295', '48 Ursae Majoris', 'Merak'),
    StarCoordinate('HR-4301', '50 Ursae Majoris', 'Dubhe'),
    StarCoordinate('HR-3757', '23 Ursae Majoris', '23 UMa'),
    StarCoordinate('HR-3323', '01 Ursae Majoris', 'ο UMa'),
    StarCoordinate('HR-3888', '29 Ursae Majoris', 'υ UMa')
]

ursa_pair = [
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

base_url = 'http://localhost:8090'

def decimalToDegrees(x:float) -> list:
    degrees = int(x)
    minutes = (x-degrees)*60.0
    seconds = (minutes-int(minutes))*60.0
    return int(degrees), int(minutes), round(seconds, 1)

def setup_time():
    response = requests.post(f'{base_url}/api/main/time?time=2280600.9895833335')
    if(response.status_code != 200):
        raise Exception('Error setting the time')

def setup_location():
    latitude = '19.427778244018555'
    longitude = '-99.1177749633789'
    altitude = '0'
    response = requests.post(f'{base_url}/api/location/setlocationfields?latitude={latitude}&longitude={longitude}&altitude={altitude}&planet=Earth')
    if(response.status_code != 200):
        raise Exception('Error setting the location')

def get_star_information(star_name):
    '''
     To-Do: check against logic of https://www.celestialprogramming.com/decimal_degrees_to_components.html
    '''
    response = requests.get(f'{base_url}/api/objects/info?name={star_name}&format=json')
    if response.status_code == 200:
        data = response.json()
        return data['vmag'], data['altitude'], data['dec']
    else:
        raise Exception(f'Could not find star with name "{star_name}".')

def print_ar_dec(ar, dec):
    ar_hours, ar_minutes, ar_seconds = decimalToDegrees(ar)
    dec_hours, dec_minutes, dec_seconds = decimalToDegrees(dec)
    ar_str = f'{ar} ({ar_hours}h {ar_minutes}m {ar_seconds}s)'
    dec_str = f'{dec} ({dec_hours}h {dec_minutes}m {dec_seconds}s)'
    print(f'AR/Dec (en fecha): {ar_str} / {dec_str}\n') 

def fill_with_magnitude_and_ecuatorial_coordinates(stars:list[StarCoordinate]):

    for i in range(0, len(stars)):

        try:
            print(f'Estrella: {stars[i].common_name}')
            print('-----------')
            mag, ar, dec = get_star_information(stars[i].common_name)
            stars[i].magnitude = mag
            stars[i].ar = ar
            stars[i].dec = dec

            print(f'Magnitud: {stars[i].magnitude:.2f}')
            print_ar_dec(stars[i].ar, stars[i].dec)

        except Exception as e:
            print(f'{str(e)}\n')

if __name__ == '__main__':
    setup_time()
    setup_location()
    fill_with_magnitude_and_ecuatorial_coordinates(ursa_major_mapping)

    

    
