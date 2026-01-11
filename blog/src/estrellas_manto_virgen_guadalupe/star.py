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

    def decimal_to_degrees_minutes_seconds(self, x:float) -> list:
        degrees = int(x)
        minutes = (x-degrees)*60.0
        seconds = (minutes-int(minutes))*60.0
        return int(degrees), int(minutes), round(seconds, 1)

    def print(self):
        ar_hours, ar_minutes, ar_seconds = self.decimal_to_degrees_minutes_seconds(self.ar)
        dec_hours, dec_minutes, dec_seconds = self.decimal_to_degrees_minutes_seconds(self.dec)
        ar_str = f'{self.ar} ({ar_hours}h {ar_minutes}m {ar_seconds}s)'
        dec_str = f'{self.dec} ({dec_hours}° {dec_minutes}m {dec_seconds}s)'
        print(f'AR/Dec (en fecha): {ar_str} / {dec_str}\n') 