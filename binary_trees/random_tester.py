from generator import Generator
from random_tree import RandomTree
import numpy as np
from timeit import default_timer as timer
class BSTTester:
    def __init__(self) -> None:
        self.test_sizes = [100, 500, 1000, 3000, 5000, 7000, 10000, 20000, 40000, 50000]
        self.generator = Generator()


    def start_test(self):
        self.creating_tree_test()
        self.find_minimum_test()
        self.balance_tree_test()

    def creating_tree_test(self):
        print("Tworzenie drzewa test: \n")
        for test_size in self.test_sizes:
            times = []
            for _ in range(10):
                start = timer()
                tree = RandomTree(self.generator.generate(test_size))
                end = timer()
                times.append(end-start)
            print(f"Elements: {test_size}, execution time: {np.mean(times)} deviation: {np.std(times)}")
        print("-----------------------------------------\n")
    
    def find_minimum_test(self):
        print("Wyszukiwanie minimalnej wartości: \n")
        for test_size in self.test_sizes:
            times = []
            for _ in range(10):
                tree = RandomTree(self.generator.generate(test_size))
                start = timer()
                tree.get_min()
                end = timer()
                times.append(end-start)
            print(f"Elements: {test_size}, execution time: {np.mean(times)} deviation: {np.std(times)}")
        print("-----------------------------------------\n")

    def balance_tree_test(self):
        print("Balansowanie drzewa: \n")
        for test_size in self.test_sizes:
            times = []
            for _ in range(10):
                tree = RandomTree(self.generator.generate(test_size))
                start = timer()
                tree.correct_balance(tree.root)
                end = timer()
                times.append(end-start)
            print(f"Elements: {test_size}, execution time: {np.mean(times)} deviation: {np.std(times)}")
        print("-----------------------------------------\n")

tester = BSTTester()
tester.start_test()