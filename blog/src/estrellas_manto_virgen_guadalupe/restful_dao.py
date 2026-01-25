'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

import requests

class RestfulDao:

    def __init__(self, base_url:str): 
        self.base_url = base_url
        self.connection_error_message = f'Error connecting to {self.base_url}. Please check Stellarium is running and the plugin for remote control is installed.'

    def post(self, url:str, body:str=None) -> requests.Response:
        try:
            response = requests.post(url, body)
        except:
            raise Exception(self.connection_error_message)
        return response

    def get(self, url:str) -> requests.Response:
        try:
            response = requests.get(url)
        except:
            raise Exception(self.connection_error_message)
        return response