from timeit import default_timer as timer

from sorter import Sorter

class HeapSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def heapify(self, array, n, i):
        #finding the largest element 
        max_v = i
        left = 2*i +1
        right = 2*i +2

        if left < n and array[i] < array[left]:
            max_v = left

        if right < n and array[max_v] < array[right]:
          max_v = right

        # If root is not largest, swap with largest and continue heapifying
        if max_v != i:
            array[i], array[max_v] = array[max_v], array[i]
            self.heapify(array, n, max_v)


    def sort(self, array):
        self.start_time = timer()
        n = len(array)

        # Build max heap
        for i in range(n//2, -1, -1):
            self.heapify(array, n, i)
        
        for i in range(n-1, 0, -1):
            # Swap
            array[i], array[0] = array[0], array[i]
            # Heapify root element
            self.heapify(array, i, 0)

        self.end_time = timer()

        return array
    
    def get_info(self):
        return "Heap sorter test suite\n"
