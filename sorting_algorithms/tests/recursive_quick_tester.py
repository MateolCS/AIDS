from tester import Tester

from recursive_quick_sorter import RecursiveQuickSorter

class RecursiveQuickTester(Tester):
    def __init__(self, sorter):
        super().__init__(sorter)

    def get_test_info(self):
        print(self.sorter.get_info())
        return super().get_test_info()


recursive_quick_tester = RecursiveQuickTester(RecursiveQuickSorter)
recursive_quick_tester.get_test_info()