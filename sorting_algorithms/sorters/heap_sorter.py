from sorter import Sorter

class HeapSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def heapify(self, array, n, i):
        max_v = i
        left = 2*i +1
        right = 2*i +2

        if left < n and array[i] < array[left]:
            max_v = left

        if right < n and array[max_v] < array[right]:
          max_v = right

        if max_v != i:
            array[i], array[max_v] = array[max_v], array[i]
            self.heapify(array, n, max_v)


    def sort(self, array):
        n = len(array)

        for i in range(n//2, -1, -1):
            self.heapify(array, n, i)
        
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)

        return array
