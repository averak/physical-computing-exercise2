import unittest
import numpy as np
import key.vector as key_vector
from key.vector import KeyVector


class TestKey(unittest.TestCase):
    def setUp(self):
        self.length = 30
        self.key_vector = KeyVector(self.length)

    def test_vector(self):
        self.key_vector.reset()
        vector = self.key_vector.vector
        self.assertTrue(isinstance(vector, np.ndarray))
        self.assertEqual(len(vector), self.length)

    def test_vector_push(self):
        self.key_vector.reset()
        self.key_vector.push(100)
        vector = self.key_vector.vector
        self.assertEqual(vector[0], 100)

    '''
    def test_preprocessing(self):
        x = np.array([[1, 1, 1]])
        x = key_vector.preprocessing(x)[0]
        self.assertEqual(key_vector.VEC_SIZE, len(x))
        self.assertEqual([1 / 226], x[0])
    '''
