import tensorflow.keras.layers as layers
from tensorflow.keras import Model


def make_nnet(input_shape, n_class):
    input_layer = layers.Input(shape=input_shape)

    hidden_layer1 = layers.Dense(64, activation='relu')(input_layer)
    drop_layer1 = layers.Dropout(0.5)(hidden_layer1)
    hidden_layer2 = layers.Dense(64, activation='relu')(drop_layer1)
    drop_layer2 = layers.Dropout(0.5)(hidden_layer2)

    output_layer = layers.Dense(n_class, activation='softmax')(drop_layer2)

    return Model(inputs=input_layer, outputs=output_layer)
