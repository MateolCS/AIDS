from generator import Generator

import numpy as np 
class AShapeGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n) -> list:
        array = []
        for i in range(n // 2):
            array.append(2 * i + 1)
        for i in range(n // 2, n):
            array.append(2 * (n - i))
        return array
        