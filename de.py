import random

class De:
    def __init__(self, minim,maxim):
        self._min=minim
        self._max=maxim

    @property
    def minimum(self):
        return self._min
    @property
    def maximum(self):
        return self._max
    def lancer_de(self,minim,maxim):
        return random.randint(self._min, self._max)