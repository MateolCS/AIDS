from timeit import default_timer as timer

from sorter import Sorter
class MergeSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)
        self.merge_count = 0

    def sort(self, array):
        self.merge_count = 0
        self.start_time = timer()
        if len(array) <= 1:
            return array
        
        # Split the array into two halves
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        # Recursively sort each half
        left_half = self.sort(left_half)
        right_half = self.sort(right_half)
        
        # Merge the sorted halves
        self.end_time = timer()
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        self.merge_count += 1
        result = []
        left_index = right_index = 0
        
        # Compare elements from both arrays and add the smaller one to the result
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        
        # Add remaining elements from left array
        while left_index < len(left):
            result.append(left[left_index])
            left_index += 1
        
        # Add remaining elements from right array
        while right_index < len(right):
            result.append(right[right_index])
            right_index += 1
        
        return result
    
    def get_info(self):
        return "Merge sorter test suite"
    
    def get_merge_count(self):
        return self.merge_count