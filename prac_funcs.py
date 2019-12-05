import numpy as np


def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s


def image2vector(image):
    if (type(image) != np.ndarray or len(image.shape) != 3):
        return NULL
    image = image.reshape((image.shape[0]*image.shape[1], v.shape[2]))
    return image


def normalizeRows(x):
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    x = x/x_norm
    return x
