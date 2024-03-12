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

class ManualTester():
    def __init__(self, sorter):
        self.random_generator = RandomGenerator()
        self.ashape_generator = AShapeGenerator()
        self.vshape_generator = VShapeGenerator()
        self.increasing_generator = IncreasingGenerator()
        self.decreasing_generator = DecreasingGenerator()
        self.sorter = sorter()

    
    def test(self):
        while(True):
            print("Podaj n:")
            n = int(input())
            print('Wybierz generator')
            print("A - akształtny")
            print("V - vkształtny")
            print("I - rosnący")
            print("D - malejący")
            print("R - losowy")
            choice = input()
            print("----------------")

            if choice.upper() == 'A':
                print(self.ashape_test(n))
            elif choice.upper() == 'V':
                print(self.vshape_test(n))
            elif choice.upper() == 'I':
                print(self.increasing_test(n))
            elif choice.upper() == 'D':
                print(self.decreasing_test(n))
            elif choice.upper() == 'R':
                print(self.random_test(n))
            else:
                print("Invalid option")


        

    def random_test(self, sample_size):

        unsorted_list = self.random_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list)

        return f"Time: {self.sorter.get_time()}\n Unsorted list: {unsorted_list}\n Sorted list: {sorted_list}"
    
    def ashape_test(self, sample_size):
  

        unsorted_list = self.ashape_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy())

        return f"Time: {self.sorter.get_time()}\n Unsorted list: {unsorted_list}\n Sorted list: {sorted_list}"

    def vshape_test(self, sample_size):
     

        unsorted_list = self.vshape_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy())

        return f"Time: {self.sorter.get_time()}\n Unsorted list: {unsorted_list}\n Sorted list: {sorted_list}"

    def increasing_test(self, sample_size):
    

        unsorted_list = self.increasing_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy())

        return f"Time: {self.sorter.get_time()}\n Unsorted list: {unsorted_list}\n Sorted list: {sorted_list}"

    def decreasing_test(self, sample_size):
        unsorted_list = self.decreasing_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy())

        return f"Time: {self.sorter.get_time()}\n Unsorted list: {unsorted_list}\n Sorted list: {sorted_list}"
    
    