import matplotlib.pyplot as plt
import numpy as np
import cv2

def detect_star():
    img = cv2.imread('photo_path', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0, 0), fx=2, fy=2)
    stars = np.where(img >= 30)

    for y, x in zip(stars[0], stars[1]):
        cv2.rectangle(img, (x - 10, y - 10), (x + 10, y + 10), (255, 255, 255), 1)

    plt.imshow(img, cmap='gray')
    plt.title('Looking for the stars on the photo')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    detect_star()
