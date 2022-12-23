# Prototyp, zderzenie centralne - Python
# Stworzone przez Adrian 'adyo'

from sys import argv
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# Wczytywanie podstawowych danych do rysowania wykresu
x1, x2 = 1, 3
x1_min, x2_max = x1, x2
    
# Wczytywanie masy obu ciał
m1, m2 = float(argv[1]), float(argv[2])

# Wczytywanie prędkości obu ciał przed zderzeniem
v1_i, v2_i = float(argv[3]), float(argv[4])

# Blokowanie niektórych wartości
if m1 < 1 or m1 > 5 or m2 < 1 or m2 > 5:
    print('Masa musi spełniać warunek: 5 < m < 1')
    exit(0)

if v1_i < 0.1 or v1_i > 50 or v2_i < 0.1 or v2_i > 50:
    print('Prędkość początkowa musi spełniać warunek: 0.1 < v_i < 50')
    exit(0)

# Obliczanie prędkości końcowych przy pomocy
# zasady zachowania pędu m1v1 + m2v2 = m1u1 + m2u2
u1 = ((m1 - m2) / (m1 + m2)) * v1_i + ((2 * m1) / (m1 + m2)) * v2_i
u2 = ((2 * m1) / (m1 + m2)) * v1_i + ((m2 - m1) / (m1 + m2)) * v2_i

# Drukowanie danych w konsoli
print('Masy ciał: m1 = {}, m2 = {}'.format(m1, m2))
print('Prędkość początkowa: v1 = {}, v2 = {}'.format(v1_i, v2_i))
print('Prędkość końcowa: u1 = {}, u2 = {}'.format(u1, u2))

# Rysowanie wykresu
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
axes.set_xlim(x1_min, x2_max)
axes.set_title('Zderzenie centralne dwóch ciał', size=17, loc='right')

scatter1, = axes.plot(x1, 0, 'o', ms=m1 * 4, label='ciało nr 1 (m={})'.format(m1))
scatter2, = axes.plot(x2, 0, 'o', ms=m2 * 4, label='ciało nr 2 (m={})'.format(m2))

# Tworzymy animację
def update(i):
    global x1, x2, u1, u2, v1_i, v2_i
    x1 = x1 + v1_i * 0.001
    x2 = x2 - v2_i * 0.001
    distance = abs(x2 - x1)

    if v1_i != 0 or v2_i != 0:
        print('Odległość ciała pierwszego od drugiego: {}'.format(distance))

    if x1 <= x1_min: v1_i = 0
    if x2 >= x2_max: v2_i = 0

    scatter1.set_data(x1, 0)
    scatter2.set_data(x2, 0)

    if distance < 0.025:
        print('Zderzenie!')
        v2_i = -u2
        v1_i = -u1

    return scatter1, scatter2

anim = FuncAnimation(fig, update, frames=200, interval=20)
plt.legend()
plt.show()
