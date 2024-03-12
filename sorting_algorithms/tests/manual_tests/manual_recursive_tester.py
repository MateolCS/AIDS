from manual_tester import ManualTester

from recursive_quick_sorter import RecursiveQuickSorter

class ManualRecursiveQuickTester(ManualTester):
    def __init__(self, sorter):
        super().__init__(sorter)


tester = ManualRecursiveQuickTester(RecursiveQuickSorter)