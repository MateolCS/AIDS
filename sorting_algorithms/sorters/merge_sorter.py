from timeit import default_timer as timer

from sorter import Sorter
class MergeSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def sort(self,array):
        self.start_time = timer()
        if len(array) > 1:

            
            r = len(array)//2
            L = array[:r]
            M = array[r:]

            
            self.sort(L)
            self.sort(M)

            i = j = k = 0

            
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1


            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1
        
        self.end_time = timer()
        return array
    
    def get_info(self):
        return "Merge sorter test suite"