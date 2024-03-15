from tester import Tester

from shell_sorter import ShellSorter
class ShellTester(Tester):
    def __init__(self, sorter):
        super().__init__(sorter)

    def get_test_info(self):
        print(self.sorter.get_info())
        return super().get_test_info()



shell_tester = ShellTester(ShellSorter)
shell_tester.get_test_info()