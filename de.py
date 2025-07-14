import random

class De:
    def __init__(self, minim,maxim):
        self._min=minim
        self._max=maxim

    @property
    def minimum(self):
        return self._min
    @property
    def max(self):
        return self._max
