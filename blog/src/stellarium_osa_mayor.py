'''
2025 Juan M. Fonseca-Solís
Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''

import requests

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

def print_star_information(star_name):
    response = requests.get(f'{base_url}/api/objects/info?name={star_name}&format=json')
    data = response.json()

    print(f'Estrella: {star_name}')
    print('-----------')
    print(f'Magnitud: {data['vmag']:.2f}')

    ar_hours, ar_minutes, ar_seconds = decimalToDegrees(data['altitude']) # working good
    dec_hours, dec_minutes, dec_seconds = decimalToDegrees(data['dec']) # working no so good...
    ar = f'{data['altitude']} ({ar_hours}h {ar_minutes}m {ar_seconds}s)'
    dec = f'{data['dec']} ({dec_hours}h {dec_minutes}m {dec_seconds}s)'
    print(f'AR/Dec (en fecha): {ar}/{dec}')
    print()

    # To-Do: check against logic of https://www.celestialprogramming.com/decimal_degrees_to_components.html

if __name__ == '__main__':
    setup_time()
    setup_location()

    for star in ['mimosa', 'alkaid']:
        print_star_information(star)
