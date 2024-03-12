import sys

from dotenv import load_dotenv
import os

load_dotenv()

generator_path = os.environ.get('GENRATOR_PATH')
sorter_path = os.environ.get('SORTER_PATH')

print(generator_path)
print(sorter_path)

sys.path.append(rf"{generator_path}")
sys.path.append(rf"{sorter_path}")

from random_generator import RandomGenerator
from ashape_generator import AShapeGenerator
from vshape_generator import VShapeGenerator
from increasing_generator import IncreasingGenerator
from decreasing_generator import DecreasingGenerator

import numpy as np

class Tester:
    def __init__(self, sorter):
        self.random_generator = RandomGenerator()
        self.ashape_generator = AShapeGenerator()
        self.vshape_generator = VShapeGenerator()
        self.increasing_generator = IncreasingGenerator()
        self.decreasing_generator = DecreasingGenerator()
        self.sorter = sorter()
        self.test_sizes = [100, 500, 1000, 3000, 5000, 7000, 10000, 20000, 40000, 50000]
        

    def random_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.random_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"
    
    def ashape_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.ashape_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"

    def vshape_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.vshape_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"

    def increasing_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.increasing_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"

    def decreasing_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.decreasing_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"


    def get_test_info(self):

        print("\nRandom order\n")

        for test_size in self.test_sizes:
            print(self.random_test(test_size))
        
        print("\nAshape\n")

        for test_size in self.test_sizes:
            print(self.ashape_test(test_size))

        print("\nVshape\n")
        
        for test_size in self.test_sizes:
            print(self.vshape_test(test_size))
        
        print("\nIncreasing order\n")

        for test_size in self.test_sizes:
            print(self.increasing_test(test_size))
        
        print("\nDecreasing order\n")

        for test_size in self.test_sizes:
            print(self.decreasing_test(test_size))
