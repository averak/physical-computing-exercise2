import unittest
import numpy as np
import nnet


VEC_LENGTH = 30
N_CLASS = 10


class TestNnet(unittest.TestCase):
    def make_nnet(self, load_weights=False):
        return nnet.make_nnet((VEC_LENGTH,), N_CLASS, load_weights)

    def compile_nnet(self, model):
        return nnet.compile_nnet(model)

    def train_nnet(self, model, x, y, save_weights=False):
        return nnet.train_nnet(model, x, y, save_weights)

    def test_make_nnet(self):
        self.make_nnet()

    def test_train_nnet(self):
        model = self.make_nnet()
        model = self.compile_nnet(model)

        # 適当なデータセットを作成
        x = []
        y = []
        for i in range(20):
            x.append([np.random.rand() for _ in range(VEC_LENGTH)])
            y.append(i % N_CLASS)

        model = self.train_nnet(model, x, y, True)

    def test_predict(self):
        model = self.make_nnet(True)
        sample_x = [np.random.rand() for _ in range(VEC_LENGTH)]
        print(nnet.predict(model, sample_x))
