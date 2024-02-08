# Równanie siecznej - Python
# Stworzone przez Adrian 'adyo' Just

import numpy as np
import matplotlib.pyplot as plt
from sympy import diff, symbols, Expr


class SecantEquation:
    def __init__(self, func: Expr, x0: float) -> None:
        self.func = func
        self._a = diff(func, x).subs(x, x0).evalf()
        self._b = -self.func.subs(x, x0).evalf()

    def display_plot(self) -> None:
        x_data = np.linspace(0.1, 5, 1000)
        fx = [self.func.subs(x, val) for val in x_data]
        gx = self._a + x_data + self._b
        plt.plot(x_data, fx)
        plt.plot(x_data, gx)
        plt.show()

    @property
    def coefficients(self) -> None:
        return f'a={float(self._a)}, b={float(self._b)}'


x = symbols("x")
eq = SecantEquation(x**2, 1)
print(eq.coefficients)
eq.display_plot()