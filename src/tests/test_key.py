import unittest
import numpy as np
import key_vector as key_vec
import key_handler as key_handler
from key_handler import KeyHandler


class TestKey(unittest.TestCase):
    def test_preprocessing(self):
        x = np.array([[1, 1, 1]])
        x = key_vec.preprocessing(x)[0]
        self.assertEqual(key_vec.VEC_SIZE, len(x))
        self.assertEqual([1 / 226], x[0])

    def test_hundler(self):
        length = 30
        key_handler = KeyHandler(length)
        self.assertEqual(key_handler.keys, [0] * length)
