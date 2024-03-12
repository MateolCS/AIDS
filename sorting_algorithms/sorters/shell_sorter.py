from timeit import default_timer as timer

from sorter import Sorter


class ShellSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def sort(self, array):
        self.start_time = timer()
        l = len(array)
        interval = len(array) // 2

        while interval > 0:
            for i in range(interval, l):
                temp = array[i]
                while i >= interval and array[i - interval] > temp:
                    array[i] = array[i - interval]
                    i -= interval
                array[i] = temp
            interval //=2
        self.end_time = timer()
        return array


    def get_time(self):
        return super().get_time()