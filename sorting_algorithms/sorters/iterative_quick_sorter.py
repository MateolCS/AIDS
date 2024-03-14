from timeit import default_timer as timer

from sorter import Sorter
import time
class IterativeQuickSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def partition(self, array, p, r):
 
        x = array[r]
 
        i = p - 1
 
        for j in range(p, r):
            if array[j] >= x:
 
                i = i + 1
 
                (array[i], array[j]) = (array[j], array[i])
 
        (array[i + 1], array[r]) = (array[r], array[i + 1])
 
        return i + 1
            

    def sort(self, array, p, r): 
  
        self.start_time = timer()

        size = r - p + 1
        stack = [0] * (size) 
  
        top = -1
  
        top = top + 1
        stack[top] = p 
        top = top + 1
        stack[top] = r 
  
        while top >= 0: 
  
            r = stack[top] 
            top = top - 1
            p = stack[top] 
            top = top - 1
  

            q = self.partition(array, p, r) 
  

            if q-1 > p: 
                top = top + 1
                stack[top] = p 
                top = top + 1
                stack[top] = q - 1
  
            if q + 1 < r: 
                top = top + 1
                stack[top] = q + 1
                top = top + 1
                stack[top] = r 

        self.end_time = timer()
        return array

    def get_info(self):
        return "Iterative quick sort tet suite\n"
    
    def get_time(self):
        return super().get_time()