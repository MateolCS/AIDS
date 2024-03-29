from generator import Generator

import numpy as np

class RandomGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n):
        return np.random.randint(1, 10*n, n, dtype=int).tolist()
        
