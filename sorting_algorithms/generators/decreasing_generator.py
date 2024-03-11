from generator import Generator

import numpy as np

class DecreasingGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n):
        return np.linspace(1, 10*n, n, dtype=int).tolist()[::-1]
        
