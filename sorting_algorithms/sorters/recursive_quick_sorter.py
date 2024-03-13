from timeit import default_timer as timer

from sorter import Sorter
import sys


sys.setrecursionlimit(1000000)
class RecursiveQuickSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def sort(self, array, p, r):
        self.start_time = timer()
        if p < r:

            q = self.partition(array, p, r)
 
            self.sort(array, p, q - 1)
 
            self.sort(array, q + 1, r)
        self.end_time = timer()

        return array

    def partition(self, array, p, r):
 
        x = array[r]
 
        i = p - 1
 
        for j in range(p, r):
            if array[j] >= x:
 
                i = i + 1
 
                (array[i], array[j]) = (array[j], array[i])
 
        (array[i + 1], array[r]) = (array[r], array[i + 1])
 
        return i + 1
    
    def get_info(self):
        return "Recursive quick sort tet suite\n"
    
    def get_time(self):
        return super().get_time()