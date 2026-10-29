"""
LEZIONE DEL 26/10/2026 - WEEK 06
"""
class Model():
    def __init__(self):
        self._valore = 0

    @property
    def valore(self):
        return self._valore
    @valore.setter
    def valore(self, v):
        self._valore = v