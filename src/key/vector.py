import numpy as np


class KeyVector:
    def __init__(self, length=None, vector=None):
        if length is None and vector is None:
            raise Exception('length / vectorのいずれかを指定してください')

        if length is None:
            self._length = len(vector)
            self._vector = list(vector)
        else:
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
