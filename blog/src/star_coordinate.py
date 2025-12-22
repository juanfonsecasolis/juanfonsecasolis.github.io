''' 
 2025 Juan M. Fonseca-Solís
 Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe
'''

class Star:

    def __init__(self, hr_name:str, flamsteed_name:str, common_name:str):
        self.hr_name = hr_name
        self.flamsteed_name = flamsteed_name
        self.common_name = common_name
        self.magnitude = None
        self.ar = None
        self.dec = None