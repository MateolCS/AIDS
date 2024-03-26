
import random


class Generator:
    def __init__(self) -> None:
        pass

    def generate(self, n):
        values = set()

        while len(values) < n:
            values.add(random.randint(1, 10*n))
        
        return list(values)
    