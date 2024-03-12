from manual_tester import ManualTester
from iterative_quick_sorter import IterativeQuickSorter

class ManualIterativeQuickTester(ManualTester):
    def __init__(self, sorter):
        super().__init__(sorter)


tester = ManualIterativeQuickTester(IterativeQuickSorter)