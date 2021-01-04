import sys
import termios
import time
import threading
import pyautogui as pgui

from .vector import KeyVector
from . import DEFAULT_DIM


class EventViewer:
    def __init__(self, dim=DEFAULT_DIM):
        self._vector = KeyVector(dim)
        self._time = time.time()

        self._run_event = threading.Event()
        self._run_event.clear()

    def _input_key(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)

        new[3] &= ~termios.ICANON
        new[3] &= ~termios.ECHO

        termios.tcsetattr(fd, termios.TCSANOW, new)
        result = sys.stdin.read(1)
        termios.tcsetattr(fd, termios.TCSANOW, old)

        return result

    def _key_viewer(self):
        while self._run_event.is_set():
            key = self._input_key()
            self._vector.push(ord(key))
            self._time = time.time()

    def start(self, limit=0.4, min_length=3):
        self._run_event.set()
        thread = threading.Thread(target=self._key_viewer)
        thread.start()
        self._vector.reset()

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

        self._run_event.clear()
        pgui.typewrite(' ')

        return self._vector
