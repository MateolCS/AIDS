from timeit import default_timer as timer

from sorter import Sorter

class HeapSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def heapify(self, array, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is greater than root
        if left < n and array[left] < array[largest]:
            largest = left

        # See if right child of root exists and is greater than largest so far
        if right < n and array[right] < array[largest]:
            largest = right

        # Change root, if needed
        if largest != i:
            array[i], array[largest] = array[largest], array[i]  # swap

            # Heapify the root.
            self.heapify(array, n, largest)


    def sort(self, array):
        self.start_time = timer()
        n = len(array)

        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(array, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]  # swap
            self.heapify(array, i, 0)
        
        self.end_time = timer()

        return array
    
    def get_info(self):
        return "Heap sorter test suite\n"


    def get_time(self):
        return super().get_time()
    
sorter = HeapSorter()
print(sorter.sort([9, 12, 4, 5]))