import numpy as np


def predict(model, x):
    pred = model.predict(x.reshape(-1, x.shape[0]))[0]
    return np.argmax(pred)
