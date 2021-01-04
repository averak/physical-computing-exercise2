import os
import datetime
import glob
import numpy as np

from .vector import KeyVector


class KeyRepository:
    def __init__(self):
        self._data_dir = 'data'

    def store(self, key_vector: KeyVector, tag: str, dump=True):
        dir_name = '%s/%s' % (self._data_dir, tag)
        file_name = '%s/%s.npy' % (
            dir_name,
            datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        )

        if dump:
            os.makedirs(dir_name, exist_ok=True)
            np.save(file_name, key_vector.vector)

    def find(self, tag: str):
        result = []

        files = glob.glob('%s/%s/*.npy' % (self._data_dir, tag))
        for f in files:
            vector = KeyVector(vector=np.load(f))
            result.append(vector)

        return result

    @property
    def tags(self):
        cols = os.listdir(self._data_dir)
        return [c for c in cols
                if os.path.isdir('%s/%s' % (self._data_dir, c))]
