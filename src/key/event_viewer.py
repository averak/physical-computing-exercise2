import sys
import time
import threading
import getch

from .vector import KeyVector
from . import DEFAULT_DIM


class EventViewer:
    def __init__(self, dim=DEFAULT_DIM):
        self._vector = KeyVector(dim)
        self._time = time.time()

        thread = threading.Thread(target=self._key_viewer)
        thread.start()
        self._start_input = False

    def _key_viewer(self):
        while True:
            key = getch.getch()

            if self._start_input:
                self._vector.push(ord(key))
                self._time = time.time()

            # esc -> exit!
            if key == '\x1b':
                break

    def start(self, limit=0.4, min_length=3):
        self._vector.reset()
        self._start_input = True

        # キー入力完了まで待機
        self._time = time.time()
        while True:
            # 待機完了 & 最低限入力された
            if (time.time() - self._time > limit and
                    self._vector.length > min_length):
                break
            # 次元数分を入力した
            if self._vector.length == self._vector.dim:
                break

            time.sleep(0.01)

        self._start_input = False

        return self._vector
