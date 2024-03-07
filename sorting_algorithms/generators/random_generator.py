from generator import Generator

import random

class RandomGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n):
        nums = []
        for _ in range(n):
            nums.append(random.randint(1, 10*n))
        return nums
        
randomizer = RandomGenerator()
print(randomizer.generate(10))