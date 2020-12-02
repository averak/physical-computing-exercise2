import unittest
import numpy as np
import key_vector


class TestVector(unittest.TestCase):
    def test_preprocessing(self):
        x = np.array([[1, 1, 1]])
        x = key_vector.preprocessing(x)[0]
        self.assertEqual(key_vector.VEC_SIZE, len(x))
        self.assertEqual([1 / 226], x[0])
