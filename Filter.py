import numpy as np
import cv2 as cv


class Filter:
    image = None
    def __init__(self, image):
        self.image = image

    def unmask(self, k):
        smoothImage = cv.blur(self.image)
        mask = self.image - smoothImage
        return self.image + k * mask

    def orderDerivatives(self, order):
        if (order == 1):
            edgeFilter = np.array([[0, -1, 0], [-1, 1, 0], [0, 0, 0]])
        elif (order == 2):
            edgeFilter = np.array([[0, 1, 0], [1, -2, 1], [0, 1, 0]])

        result = np.zeros((self.image.shape[0], self.image.shape[1]))
        cv.filter2D(self.image, result, edgeFilter)
        return result