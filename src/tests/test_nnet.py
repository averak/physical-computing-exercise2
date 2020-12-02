import unittest
import numpy as np
import nnet


VEC_LENGTH = 30
N_CLASS = 10


class TestNnet(unittest.TestCase):
    def make_dnn(self):
        return nnet.dnn((VEC_LENGTH,), N_CLASS)

    def test_make_dnn(self):
        self.make_dnn()

    def test_train_dnn(self):
        dnn = self.make_dnn()
        dnn.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'],
        )

        x = []
        y = []
        for i in range(20):
            x.append([np.random.rand() for _ in range(VEC_LENGTH)])
            y.append(i % N_CLASS)

        dnn.fit(
            np.array(x),
            np.array(y),
            batch_size=32,
            epochs=10,
            validation_split=0.1,
            verbose=0,
        )
