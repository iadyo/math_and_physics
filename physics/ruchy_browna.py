# Ruchy Browna - Python

import matplotlib.pyplot as plt
import numpy as np

def main():
    cmap = plt.cm.get_cmap('Spectral')
    lx, ly, colors = [], [], []
    npoints = 60
    x = y = 0

    for i in range(npoints):
        rad = float(np.random.uniform(0, 360)) * np.pi / 180
        x = x + 4 * np.cos(rad)
        y = y + 4 * np.sin(rad)
        x = int(round(x, 2))
        y = int(round(y, 2))

        colors.append(i / npoints)
        lx.append(x)
        ly.append(y)

    u = np.diff(lx)
    v = np.diff(ly)

    pos_x = lx[:-1] + u / 2
    pos_y = ly[:-1] + v / 2
    norm = np.sqrt(u**2 + v**2)
    
    plt.figure(figsize=(8,8))
    plt.ion()
    plt.show()

    for i in range(npoints):
        plt.scatter(lx[i:i+1], ly[i:i+1], cmap=cmap, c=cmap(colors[i:i+1]), s=100, zorder=2)
        plt.plot(lx[i-1:i+1], ly[i-1:i+1], 'C0', lw=5, zorder=1)
        plt.quiver(pos_x[i:i+1], pos_y[i:i+1], u[i:i+1] / norm[i:i+1], v[i:i+1] / norm[i:i+1], angles='xy', pivot='mid', zorder=5)
        plt.subplots_adjust(left=0.05, bottom=0.03, right=0.98, top=0.979)
        plt.pause(0.01)
        plt.draw()

if __name__ == '__main__':
    main()
