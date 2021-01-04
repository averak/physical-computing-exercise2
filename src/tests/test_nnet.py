import unittest
import numpy as np
import nnet

from key import DEFAULT_DIM


class TestNnet(unittest.TestCase):
    def setUp(self):
        self.dim = DEFAULT_DIM
        self.n_class = 10
        self.model = nnet.Model(model_file='test.h5', n_class=self.n_class)

    @unittest.skip('TESTSKIP')
    def test_train_nnet(self):
        # 適当なデータセットを作成
        x = []
        y = []
        for i in range(20):
            x.append([np.random.rand() for _ in range(self.dim)])
            y.append(i % self.n_class)

        self.model.train(x, y, save_weights=True)

    def test_predict(self):
        sample_x = [np.random.rand() for _ in range(self.dim)]
        self.model.predict(np.array(sample_x))
