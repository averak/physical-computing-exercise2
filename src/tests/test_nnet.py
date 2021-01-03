import unittest
import numpy as np
import nnet
from key import DEFAULT_LENGTH


class TestNnet(unittest.TestCase):
    def setUp(self):
        self.length = DEFAULT_LENGTH
        self.n_class = 10
        self.model = nnet.Model(model_file='test.h5')

    def test_train_nnet(self):
        # 適当なデータセットを作成
        x = []
        y = []
        for i in range(20):
            x.append([np.random.rand() for _ in range(self.length)])
            y.append(i % self.n_class)

        self.model.train(x, y, save_weights=True)

    def test_predict(self):
        sample_x = [np.random.rand() for _ in range(self.length)]
        self.model.predict(sample_x)
