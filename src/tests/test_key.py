import unittest
import numpy as np
import key.vector as key_vector
from key.vector import KeyVector
from key.handler import KeyHandler


class TestKey(unittest.TestCase):
    def test_vector(self):
        length = 30
        key_vec = KeyVector(length)
        self.assertEqual(key_vec.vector, [0] * length)

    def test_preprocessing(self):
        x = np.array([[1, 1, 1]])
        x = key_vector.preprocessing(x)[0]
        self.assertEqual(key_vector.VEC_SIZE, len(x))
        self.assertEqual([1 / 226], x[0])
