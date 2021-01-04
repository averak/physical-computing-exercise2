import numpy as np


def predict(model, x):
    return np.argmax(model.predict([list(x)])[0])
