from tester import Tester

from iterative_quick_sorter import IterativeQuickSorter

class IterativeQuickTester(Tester):
    def __init__(self, sorter):
        super().__init__(sorter)

    def get_test_info(self):
        print(self.sorter.get_info())
        return super().get_test_info()


iterative_quick_tester = IterativeQuickTester(IterativeQuickSorter)
iterative_quick_tester.get_test_info()