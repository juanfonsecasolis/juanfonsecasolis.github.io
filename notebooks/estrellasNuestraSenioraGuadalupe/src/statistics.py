'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''

import numpy as np

def pearson_correlation(x:list[float], y:list[float]) -> float:
        return 100.0 * np.cov(x,y, bias=True)[0][1]/(np.std(x)*np.std(y)) # 'bias=True' para normalizar por 1/N