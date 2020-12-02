import numpy as np


def predict(model, x):
    vec_length = model.input_shape[1]

    # ベクトルを固定長に変換
    x = x[:vec_length]
    x += [0] * (vec_length - len(x))

    return np.argmax(model.predict([x])[0])
