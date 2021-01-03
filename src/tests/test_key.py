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
        self.assertEqual(self.length, len(vector))

    def test_vector_push(self):
        self.key_vector.reset()
        self.key_vector.push(100)
        self.key_vector.push(200)
        self.key_vector.push(300)
        vector = self.key_vector.vector
        self.assertEqual(100, vector[0])
        self.assertEqual(200, vector[1])
        self.assertEqual(300, vector[2])

    def test_preprocessing(self):
        self.key_vector.reset()
        self.key_vector.push(1)
        self.key_vector.preprocessing()
        vector = self.key_vector.vector
        self.assertEqual([1 / 226], vector[0])
