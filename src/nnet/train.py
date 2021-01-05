import numpy as np


def train_nnet(model, x, y, save_weights=False, model_path=None):
    model.fit(
        np.array(x, np.float32),
        np.array(y, np.uint8),
        batch_size=32,
        epochs=200,
        validation_split=0.1,
    )

    if save_weights and model_path is not None:
        model.save_weights(model_path)

    return model
