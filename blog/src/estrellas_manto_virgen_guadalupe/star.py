'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
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
        ar_str = f'{self.ar:.2f} ({ar_hours}h {ar_minutes}m {ar_seconds}s)'
        dec_str = f'{self.dec:.2f} ({dec_hours}° {dec_minutes}m {dec_seconds}s)'
        print(f'[{self.common_name}/{self.hr_name}/{self.flamsteed_name}] AR (en fecha): {ar_str}, DEC (en fecha): {dec_str}, mag: {self.magnitude:.2f}.') 