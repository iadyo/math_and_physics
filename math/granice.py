import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, limit


def f(x):
    return 4 / ((x - 2)**2 * (x + 2))


x0 = 2
x = symbols('x')
solution = limit(f(x), x, x0)

x_data = np.linspace(-10, 10, 1000)
y_data = f(x_data)

plt.plot(x_data, y_data)
plt.minorticks_on()
plt.axhline(solution, color='black', ls='dashed', alpha=0.5)
plt.axvline(x0, color='black', ls='dashed', alpha=0.5)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title(
    f'Gdy x "zbliża się" do {x0}, f(x) "zbliża się" do {solution}\n$\\lim_{{x \\to {x0}}} f(x)$ = {solution}'
)
# plt.yscale('log')
plt.show()
