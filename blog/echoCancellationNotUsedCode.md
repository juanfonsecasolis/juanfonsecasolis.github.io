se (e)

Let's start by calculating the phase of the cascade filter of unit 1, for this we take multiply each transfer function with a 1 ($z^D/z^D$):

$$
H(z) = \frac{(1-0.7 z^{50})}{(z^{50}-0.7)}\frac{(1-0.66 z^{40})}{(z^{40}-0.66)}\frac{(1-0.63175 z^{32})}{(z^{32}-0.63175)},
$$

and use the `scipy.signal.freqz_zpk` function to specify the zeros, poles, and gain

import scipy.signal
from sympy import pprint, Symbol, expand, simplify, solve, Poly, re, im, atan, lambdify
import numpy as np

z = Symbol('z')
Hnum = (1-0.7*z**50)*(1-0.665*z**40)*(1-0.63175*z**32)
Hden = (z**50-0.7)*(z**40-0.665)*(z**32-0.63175)

phase = atan(im(Hnum)/re(Hnum)) - atan(im(Hden)/re(Hden))
#pprint(phase)

N = 100
x = np.linspace(-np.pi,np.pi,N)
y = np.zeros(N)
f = lambdify(z,phase)
for n in range(0,N):
    y[n] = f(x[n])

    
pylab.plot(x,y)

#pprint(expand(Hd))

#num = list(Poly(Hnum).all_coeffs())
#den = list(Poly(Hden).all_coeffs())

#signal.TransferFunction(num, den)
#print(signal)

#w, h = scipy.signal.freqz(np.flip(b),np.flip(a))
#ylab.plot(w, np.angle(h)) # we don't want to have discontinuities around the -pi to pi interval

2. http://eeweb.poly.edu/iselesni/EL6113/matlab_examples/frequency_response_demo/html/frequency_response_demo.html
3. http://www.ee.ic.ac.uk/pcheung/teaching/ee2_signals/Lecture%208%20-%20Frequency%20Response.pdf
