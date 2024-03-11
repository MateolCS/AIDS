from tester import Tester

from merge_sorter import MergeSorter

class MergeTester(Tester):
    def __init__(self, sorter):
        super().__init__(sorter)

    def get_test_info(self):
        print(self.sorter.get_info())
        return super().get_test_info()



merge_tester = MergeTester(MergeSorter)
merge_tester.get_test_info()