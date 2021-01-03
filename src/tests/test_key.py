import unittest
import numpy as np
import key.vector as key_vector
from key.handler import KeyHandler


class TestKey(unittest.TestCase):
    def test_preprocessing(self):
        x = np.array([[1, 1, 1]])
        x = key_vector.preprocessing(x)[0]
        self.assertEqual(key_vector.VEC_SIZE, len(x))
        self.assertEqual([1 / 226], x[0])

    def test_handler(self):
        length = 30
        key_handler = KeyHandler(length)
        self.assertEqual(key_handler.keys, [0] * length)
