import numpy as np


def train_nnet(model, x, y, batch_size=32, epochs=20):
    model.fit(
        np.array(x),
        np.array(y),
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.1,
    )
    return model
