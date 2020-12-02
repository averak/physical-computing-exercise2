import unittest
import numpy as np
import nnet

VEC_LENGTH = 30
N_CLASS = 10


class TestNnet(unittest.TestCase):
    def setUp(self):
        self.model = nnet.Model()

    def test_train_nnet(self):
        # 適当なデータセットを作成
        x = []
        y = []
        for i in range(20):
            x.append([np.random.rand() for _ in range(VEC_LENGTH)])
            y.append(i % N_CLASS)

        self.model.train(x, y, True)

    def test_predict(self):
        sample_x = [np.random.rand() for _ in range(VEC_LENGTH)]
        self.model.predict(sample_x)
