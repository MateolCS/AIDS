from generator import Generator

class AShapeGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n) -> list:
        nums = [0 for _ in range(n)]
        print(nums)
        for i in range(n//2):
            nums[i] = 2*i+ 1
            
        for i in range(n//2, n):
            nums[i] = 2*(n-i)

        return nums
        