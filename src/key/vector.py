import copy
import numpy as np

from . import DEFAULT_DIM


class KeyVector:
    def __init__(self, dim=DEFAULT_DIM, vector=None):
        if vector is None:
            self._dim = dim
            self._vector = []
        else:
            self._dim = len(vector)
            self._vector = list(vector)
        self._length = 0

        self.reset()

    def reset(self):
        self._vector = []
        self._length = 0

    def push(self, key: int):
        if self.length < self.dim:
            self._vector.append(key)
            self._length += 1

    def preprocessing(self):
        max_key = 226

        def proc(lamb): return [lamb(key) for key in self.vector]

        # 外れ値処理
        self._vector = proc(lambda key: 0 if key < 0 else key)
        self._vector = proc(lambda key: 0 if key > max_key else key)

        # 正規化
        if np.sum(self.vector > 1):
            self._vector = proc(lambda key: key / max_key)

    @property
    def dim(self):
        return self._dim

    @property
    def vector(self):
        result = copy.deepcopy(self._vector)
        result += [0] * (self.dim - self.length)
        return np.array(result)[:self.dim]

    @property
    def length(self):
        return self._length
