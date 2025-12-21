'''
2025 Juan M. Fonseca-Solís
Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''

import requests
import numpy as np

ursa_major_mapping = [
    { 'hr_classification': 'HR-5191', 'flamsteed': '85 Ursae Majoris', 'name': 'Alkaid'},
    { 'hr_classification': 'HR-5054', 'flamsteed': '79 Ursae Majoris', 'name': 'Mizar A'},
    { 'hr_classification': 'HR-4905', 'flamsteed': '77 Ursae Majoris', 'name': 'Alioth'},
    { 'hr_classification': 'HR-4660', 'flamsteed': '69 Ursae Majoris', 'name': 'Megrez'},
    { 'hr_classification': 'HR-4554', 'flamsteed': '64 Ursae Majoris', 'name': 'Phecda'},
    { 'hr_classification': 'HR-4295', 'flamsteed': '48 Ursae Majoris', 'name': 'Merak'},
    { 'hr_classification': 'HR-4301', 'flamsteed': '50 Ursae Majoris', 'name': 'Dubhe'},
    { 'hr_classification': 'HR-3757', 'flamsteed': '23 Ursae Majoris', 'name': '23 UMa'},
    { 'hr_classification': 'HR-3323', 'flamsteed': '01 Ursae Majoris', 'name': 'ο UMa'},
    { 'hr_classification': 'HR-3888', 'flamsteed': '29 Ursae Majoris', 'name': 'υ UMa'}
]

ursa_pais = [
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
    response = requests.get(f'{base_url}/api/objects/info?name={star_name}&format=json')
    if response.status_code == 200:
        data = response.json()
        return data['vmag'], data['altitude'], data['dec']
    else:
        raise Exception(f'Could not find star with name "{star_name}".')

    # To-Do: check against logic of https://www.celestialprogramming.com/decimal_degrees_to_components.html

def print_ar_dec(ar, dec):
    ar_hours, ar_minutes, ar_seconds = decimalToDegrees(ar)
    dec_hours, dec_minutes, dec_seconds = decimalToDegrees(dec)
    ar_str = f'{ar} ({ar_hours}h {ar_minutes}m {ar_seconds}s)'
    dec_str = f'{dec} ({dec_hours}h {dec_minutes}m {dec_seconds}s)'
    print(f'AR/Dec (en fecha): {ar_str} / {dec_str}\n')

if __name__ == '__main__':
    setup_time()
    setup_location()

    for i in range(0, len(ursa_major_mapping)):

        try:
            star_name = ursa_major_mapping[i]['name']
            print(f'Estrella: {star_name}')
            print('-----------')
            mag, ar, dec = get_star_information(star_name)
            ursa_major_mapping[i]['mag'] = mag
            ursa_major_mapping[i]['ar'] = ar
            ursa_major_mapping[i]['dec'] = dec

            print(f'Magnitud: {mag:.2f}')
            print_ar_dec(ar, dec)

        except Exception as e:
            print(f'{str(e)}\n')
