# Prototyp, Układ Słoneczny - Python

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import math

class Planet:
    def __init__(self, name, mass, da, db, speed, color):
        self.name = name
        self.mass = mass
        self.da = da
        self.db = db
        self.speed = speed
        self.color = color

    def get_radius(self, x, y):
        return math.sqrt(x**2 + y**2) * 149_597_871

def main():
    mercury = Planet('Mercury', 3.285, 0.3870993, 0.37882610063537236, 5, '#B7B8B9')
    venus = Planet('Venus', 4.867, 0.723336, 0.7233193745096448, 3, '#FFC649')
    earth = Planet('Earth', 5.98, 0.999995, 0.9998554022971552, 1, '#34A56F')
    mars = Planet('Mars', 6.39, 1.52371, 1.5170507835579325, 0.9, 'red')
    jupiter = Planet('Jupiter', 1.899, 5.2029, 5.196802374180633, 0.2, 'gray')
    saturn = Planet('Saturn', 5.683, 9.537, 9.523136429645305, 0.12, '#C4D0B0')
    uranus = Planet('Uran', 8.6832, 19.189, 19.16755863227479, 0.05, '#e1eeee')
    neptune = Planet('Neptune', 1.0243, 30.0699, 30.068790579140014, 0.012, '#5b5ddf')

    planets = [jupiter, saturn, neptune, uranus, earth, mercury, venus, mars]

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 10))
    axes.set_xlim(-33, 33)
    axes.set_ylim(-33, 33)
    axes.set_title('Solar System', size=17, loc='right')
    fig.tight_layout()

    axes.plot(0.0005682653974978802, 0, 'C1*', ms=20, label='The Sun')
    
    xt = []
    for i in range(len(planets)):
        planets.sort(key=lambda x: x.da)
        temp, = plt.plot([], [], marker='o', ls='', c=planets[i].color, ms=planets[i].mass, label=planets[i].name)
        xt.append(temp)

    xt = tuple(xt)
    axes.legend()

    def init():
        for i in range(len(planets)): xt[i].set_data([], [])
        return xt

    def update(i):
        for m in range(len(planets)):
            alfa = np.array([np.pi / 180 * i]) * planets[m].speed
            x = planets[m].da * np.cos(alfa)
            y = planets[m].db * np.sin(alfa)
            xt[m].set_data(x, y)

            print('Ilość km od Słońca ({}) to {} km'.format(planets[m].name, planets[m].get_radius(x, y)))
        print('-' * 50)
        return xt

    anim = FuncAnimation(fig, update, init_func=init, frames=2000, interval=5, blit=True)
    plt.show()

if __name__ == '__main__':
    main()
