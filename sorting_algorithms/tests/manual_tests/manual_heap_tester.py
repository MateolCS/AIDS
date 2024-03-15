from manual_tester import ManualTester
from heap_sorter import HeapSorter

class ManualHeapTester(ManualTester):
    def __init__(self, sorter):
        super().__init__(sorter)


    def random_test(self, sample_size):

        unsorted_list = self.random_generator.generate(sample_size)
        sorted_list = self.sorter.sort(unsorted_list.copy())

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


tester = ManualHeapTester(HeapSorter)
tester.test()