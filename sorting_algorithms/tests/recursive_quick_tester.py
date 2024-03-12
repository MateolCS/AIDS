from tester import Tester

import sys
sys.setrecursionlimit(500000000)

import numpy as np

from recursive_quick_sorter import RecursiveQuickSorter

class RecursiveQuickTester(Tester):
    def __init__(self, sorter):
        super().__init__(sorter)

    def random_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.random_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list, 0, sample_size-1)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"
    
    def ashape_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.ashape_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list, 0, sample_size-1)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"

    def vshape_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.vshape_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list, 0, sample_size-1)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"

    def increasing_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.increasing_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list, 0, sample_size-1)
            times.append(self.sorter.get_time())

        return f"Sample size {sample_size}, average time {np.mean(times)}"

    def decreasing_test(self, sample_size):
        times = []

        for _ in range(10):
            unsorted_list = self.decreasing_generator.generate(sample_size)
            sorted_list = self.sorter.sort(unsorted_list, 0, sample_size-1)
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


recursive_quick_tester = RecursiveQuickTester(RecursiveQuickSorter)
recursive_quick_tester.get_test_info()