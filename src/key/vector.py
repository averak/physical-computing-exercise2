import copy
import numpy as np

from . import DEFAULT_LENGTH


class KeyVector:
    def __init__(self, length=DEFAULT_LENGTH, vector=None):
        if vector is None:
            self._length = length
            self._vector = []
        else:
            self._length = len(vector)
            self._vector = list(vector)
        self._cnt = 0

        self.reset()

    def reset(self):
        self._vector = []
        self._cnt = 0

    def push(self, key: int):
        if self.cnt < self.length:
            self._vector.append(key)
            self._cnt += 1

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
    def length(self):
        return self._length

    @property
    def vector(self):
        result = copy.deepcopy(self._vector)
        result += [0] * (self.length - self.cnt)
        return np.array(result)

    @property
    def cnt(self):
        return self._cnt
