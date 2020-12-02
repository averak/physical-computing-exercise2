import unittest
import numpy as np
import nnet


VEC_LENGTH = 30
N_CLASS = 10


class TestNnet(unittest.TestCase):
    def make_nnet(self):
        return nnet.make_nnet((VEC_LENGTH,), N_CLASS)

    def compile_nnet(self, model):
        return nnet.compile_nnet(model)

    def train_nnet(self, model, x, y):
        return nnet.train_nnet(model, x, y)

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

        model = self.train_nnet(model, x, y)
