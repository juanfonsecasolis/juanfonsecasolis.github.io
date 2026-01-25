'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

from restful_dao import RestfulDao

class StellariumDao(RestfulDao):

    def __init__(self): 
        super().__init__('http://localhost:8090')

    def setup_time(self, time):
        response = self.post(f'{self.base_url}/api/main/time?time={time}')
        if(response.status_code != 200):
            raise Exception('Error setting the time.')

    def setup_location(self, latitude, longitude, altitude):
        response = self.post(f'{self.base_url}/api/location/setlocationfields?latitude={latitude}&longitude={longitude}&altitude={altitude}&planet=Earth')
        if(response.status_code != 200):
            raise Exception('Error setting the location.')
    
    def get_star_information(self, star_name):
        '''
        To-Do: check against logic of https://www.celestialprogramming.com/decimal_degrees_to_components.html
        '''
        response = self.get(f'{self.base_url}/api/objects/info?name={star_name}&format=json')
        if response.status_code == 200:
            data = response.json()
            return data['vmag'], data['altitude'], data['dec']
        else:
            raise Exception(f'Could not find star with name "{star_name}".')