'''
References:
1. https://www.latlong.net/place/mexico-city-mexico-3246.html
2. https://github.com/brandon-rhodes/pyephem/blob/fc11ddf3f2748db2fa4c8b0d491e169ed3d09bfc/ephem/stars.py#L8
'''

import ephem

ursa_major_mapping = {
    'HR-5191': {'flamsteed': '85 Ursae Majoris', 'name': 'Alkaid'},
    #'HR-5054': {'flamsteed': '79 Ursae Majoris', 'name': 'Mizar A'},
    'HR-4905': {'flamsteed': '77 Ursae Majoris', 'name': 'Alioth'},
    'HR-4660': {'flamsteed': '69 Ursae Majoris', 'name': 'Megrez'},
    'HR-4554': {'flamsteed': '64 Ursae Majoris', 'name': 'Phecda'},
    'HR-4295': {'flamsteed': '48 Ursae Majoris', 'name': 'Merak'},
    'HR-4301': {'flamsteed': '50 Ursae Majoris', 'name': 'Dubhe'},
    #'HR-3757': {'flamsteed': '23 Ursae Majoris', 'name': '23 UMa'},
    #'HR-3323': {'flamsteed': '01 Ursae Majoris', 'name': 'ο UMa'},
    #'HR-3888': {'flamsteed': '29 Ursae Majoris', 'name': 'υ UMa'}
}

#mexico_city = ephem.city('Mexico City')
#mexico_city = ephem.Observer()
#mexico_city.lat, mexico_city.lon = '19.451054', '-99.125519' # Ciudad de México
mexico_city = ephem.Mars()

for start_name_hr in ursa_major_mapping.keys():

    star_name = ursa_major_mapping[start_name_hr]['name']
    star = ephem.star(star_name)
    
    for date in ['1531/12/12 06:45:00', '2025/06/01 06:45:00']:
        
        mexico_city.date = date
        star.compute(mexico_city)
        print(f'{date} - {star_name} - ra: {star._ra}, dec: {star._dec}')
    
    print('\n---')