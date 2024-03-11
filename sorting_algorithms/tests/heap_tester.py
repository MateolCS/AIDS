from tester import Tester

from heap_sorter import HeapSorter

class HeapTester(Tester):
    def __init__(self, sorter):
        super().__init__(sorter)

    def get_test_info(self):
        print(self.sorter.get_info())
        return super().get_test_info()


heap_tester = HeapTester(HeapSorter)
heap_tester.get_test_info()