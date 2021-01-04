import unittest
import numpy as np

from key.vector import KeyVector
from key.repository import KeyRepository


class TestKey(unittest.TestCase):
    def setUp(self):
        self.key_vector = KeyVector()
        self.key_repository = KeyRepository()

    def test_vector(self):
        self.key_vector.reset()
        vector = self.key_vector.vector
        self.assertTrue(isinstance(vector, np.ndarray))
        self.assertEqual(self.key_vector.dim, len(vector))

    def test_vector_push(self):
        self.key_vector.reset()
        self.key_vector.push(100)
        self.key_vector.push(200)
        self.key_vector.push(300)
        vector = self.key_vector.vector
        self.assertEqual(100, vector[0])
        self.assertEqual(200, vector[1])
        self.assertEqual(300, vector[2])
        self.assertEqual(3, self.key_vector.length)

    def test_preprocessing(self):
        self.key_vector.reset()
        self.key_vector.push(100)
        self.key_vector.push(-100)
        self.key_vector.push(1000)
        self.key_vector.preprocessing()
        vector = self.key_vector.vector
        self.assertEqual(0, np.sum(vector < 0))
        self.assertEqual(0, np.sum(vector > 1))

    def test_repository(self):
        self.key_repository.store(self.key_vector, '0', False)
        self.assertTrue(isinstance(self.key_repository.find('0'), list))
        self.assertTrue(isinstance(self.key_repository.tags, list))

    @unittest.skip('TESTSKIP')
    def test_event_viewer(self):
        from key.event_viewer import EventViewer
        viewer = EventViewer()
        print('start!')
        viewer.start()
