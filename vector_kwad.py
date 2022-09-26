# Przesunięcie funkcji kwadratowej o wektor - Python

import matplotlib.pyplot as plt
import numpy as np
from sys import argv

def f(x, a, b, c): return a*x**2 + b*x + c

def main(coeffs):
    a, b, c = float(coeffs[1]), float(coeffs[2]), float(coeffs[3])
    vec_p, vec_q = float(coeffs[4]), float(coeffs[5])

    print('f(x) = {}x^2 + {}x + {}'.format(a, b, c))
    print('v->[{},{}]'.format(vec_p, vec_q))
    
    x = np.linspace(-10, 10, 10000)
    x0 = (a*vec_p**2 - b*vec_p + vec_q) / (2*a*vec_p)
    print('x0={}'.format(x0))

    plt.axvline(x0, alpha=0.25, c='gray')
    vec_form = f(x-vec_p, a, b, c) + vec_q
    
    plt.plot(x, f(x, a, b, c), label='f(x) = {}x$^2$ + {}x + {}'.format(a, b, c))
    plt.plot(x, vec_form, '--', label='$\\vecv=$[{},{}]'.format(vec_p, vec_q))
    plt.plot(x0, f(x0, a, b, c), 'o', ms=9)

    plt.legend()
    plt.title('Przesunięcie funkcji f(x) o wektor [{},{}]'.format(vec_p, vec_q))
    plt.show()

if __name__ == '__main__':
    main(argv)
