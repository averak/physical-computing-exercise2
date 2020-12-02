import unittest
import numpy as np
import nnet
from key_vector import VEC_SIZE

N_CLASS = 10


class TestNnet(unittest.TestCase):
    def setUp(self):
        self.model = nnet.Model(model_file='test.h5')

    def test_train_nnet(self):
        # 適当なデータセットを作成
        x = []
        y = []
        for i in range(20):
            x.append([np.random.rand() for _ in range(VEC_SIZE)])
            y.append(i % N_CLASS)

        self.model.train(x, y, save_weights=True)

    def test_predict(self):
        sample_x = [np.random.rand() for _ in range(VEC_SIZE)]
        self.model.predict(sample_x)
