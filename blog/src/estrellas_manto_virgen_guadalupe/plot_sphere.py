'''
  2025-2026 Juan M. Fonseca-Solís.
  Estrellas al momento de la impregnación de Nuestra Señora de Guadalupe, un12 de diciembre
  de 1531 a las 6:45 am en la ciudad de México.
'''
import numpy as np
import matplotlib.pylab as plt

def plot_sphere(fig, ax, r:int=1, must_show:bool=True):
    all_lambdas = np.linspace(-np.pi,np.pi,10)
    all_phis = np.linspace(-np.pi,np.pi,10)

    for one_lambda in all_lambdas:
        for one_phi in all_phis:
            x = r * np.sin(one_lambda) * np.cos(one_phi)
            y = r * np.sin(one_lambda) * np.sin(one_phi)
            z = r * np.cos(one_lambda)
            ax.scatter(x, y, z, color='blue', marker='.')
    if must_show:
        plt.show()

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plot_sphere(fig, ax)