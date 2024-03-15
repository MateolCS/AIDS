from manual_tester import ManualTester
from iterative_quick_sorter import IterativeQuickSorter

class ManualIterativeQuickTester(ManualTester):
    def __init__(self, sorter):
        super().__init__(sorter)


    def random_test(self, sample_size):

        unsorted_list = self.random_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy(), 0, sample_size-1)

        return f"Time: {self.sorter.get_time()}"
    
    def ashape_test(self, sample_size):
  

        unsorted_list = self.ashape_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy(), 0, sample_size-1)

        return f"Time: {self.sorter.get_time()}"

    def vshape_test(self, sample_size):
     
        unsorted_list = self.vshape_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy(), 0, sample_size-1)

        return f"Time: {self.sorter.get_time()}"

    def increasing_test(self, sample_size):
    

        unsorted_list = self.increasing_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy(), 0, sample_size-1)

        return f"Time: {self.sorter.get_time()}"

    def decreasing_test(self, sample_size):
        unsorted_list = self.decreasing_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy(), 0, sample_size-1)

        return f"Time: {self.sorter.get_time()}"

tester = ManualIterativeQuickTester(IterativeQuickSorter)
tester.test()