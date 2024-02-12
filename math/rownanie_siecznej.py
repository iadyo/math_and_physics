# Równanie siecznej - Python
# Stworzone przez Adrian 'adyo' Just

import numpy as np
import matplotlib.pyplot as plt
from sympy import diff, symbols, Expr


class SecantEquation:
    def __init__(self, func: Expr, x0: float) -> None:
        self.func = func
        self._a = diff(func, x).subs(x, x0).evalf()
        self._b = self.func.subs(x, x0) - self._a * x0

    def display_plot(self) -> None:
        x_data = np.linspace(-5, 5, 1000)
        fx = [self.func.subs(x, val) for val in x_data]
        gx = self._a * x_data + self._b
        plt.plot(x_data, fx)
        plt.plot(x_data, gx)
        plt.show()

    @property
    def coefficients(self) -> None:
        return f'a={float(self._a)}, b={float(self._b)}'


x = symbols("x")
eqs = [SecantEquation(x**3 + 5*x**2 + 3*x + 8, -1),
       SecantEquation((1/3)*x**3 - 9*x - 1/3, -2),
       SecantEquation(x**3 - 6*x**2 + 12*x - 4, 0),
       SecantEquation(x**2, 1)]


for idx, eq in enumerate(eqs):
    print(f'plot nr. {idx + 1}/{len(eqs)}) {eq.coefficients}')
    eq.display_plot()
