from generator import Generator

import numpy as np 
class AShapeGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n) -> list:
        middle = 10*n//2
        increase = np.arange(middle)
        decrease = np.arange(middle, 1, -1)

        return np.concatenate((increase, decrease)).tolist()
        