import numpy as np

class KeyHandler:
    def __init__(self, length):
        self._length = length
        self._keys = []

        self.reset()

    def reset(self):
        self._keys = [0] * self._length

    @property
    def keys(self):
        return self._keys
