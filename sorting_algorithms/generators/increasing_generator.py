from generator import Generator

import numpy as np

class IncreasingGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n):
        return np.linspace(1, 10*n, n, dtype=int)
        
