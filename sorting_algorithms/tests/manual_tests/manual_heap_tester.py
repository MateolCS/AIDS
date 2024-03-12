from manual_tester import ManualTester
from heap_sorter import HeapSorter

class ManualHeapTester(ManualTester):
    def __init__(self, sorter):
        super().__init__(sorter)


tester = ManualHeapTester(HeapSorter)