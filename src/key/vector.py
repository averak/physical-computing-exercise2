import numpy as np
import datetime
import glob

DATA_DIR = 'data'
VEC_SIZE = 30


class KeyVector:
    def __init__(self, length: int):
        if length <= 0:
            raise Exception('lengthは自然数を指定してください')

        self._length = length
        self._vector = []

        self.reset()

    def reset(self):
        self._vector = []

    def push(self, key: int):
        if len(self._vector) < self.length:
            self._vector.append(key)

    def preprocessing(self):
        # 正規化
        self._vector = (lambda vec: [key / 226 for key in vec])(self.vector)

    @property
    def length(self):
        return self._length

    @property
    def vector(self):
        result = self._vector
        result += [0] * (self.length - len(result))
        return np.array(result)
