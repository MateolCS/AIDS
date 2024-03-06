from sorter import Sorter


class ShellSorter(Sorter):
    def __init__(self):
        Sorter.__init__(self)

    def sort(self, array):
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

        return array
