from random_generator import RandomGenerator
from ashape_generator import AShapeGenerator
from vshape_generator import VShapeGenerator

class Tester:
    def __init__(self, sorter) -> None:
        self.random_generator = RandomGenerator()
        self.ashape_generator = AShapeGenerator()
        self.vshape_generator = VShapeGenerator()
        self.sorter = sorter()
        self.test_sizes = [100, 500, 1000, 3000, 5000, 7000,
10000, 20000, 40000, 50000]


