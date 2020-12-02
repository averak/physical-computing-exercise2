import os
import numpy as np


def train_nnet(model, x, y, batch_size=32, epochs=20, save_weights=False):
    model.fit(
        np.array(x),
        np.array(y),
        batch_size=batch_size,
        epochs=epochs,
        validation_split=0.1,
    )

    if save_weights:
        model_path = os.path.dirname(__file__) + '/ckpt/nnet.h5'
        model.save_weights(model_path)

    return model
