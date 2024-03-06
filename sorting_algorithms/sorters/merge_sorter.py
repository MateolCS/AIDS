from sorter import Sorter
class MergeSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def sort(self,array):
        if len(array) == 1:
            return array
        
        mid = len(array)//2

        left = array[mid:]
        right = array[:mid]

        sorted_array = []

        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sorted_array.append(left.pop(0))
            else:
                sorted_array.append(right.pop(0))
        
        return right + sorted_array + left