from generator import Generator

class VShapeGenerator(Generator):

    def __init__(self):
        super().__init__()

    def generate(self, n) -> list:
        nums = [0 for _ in range(n)]

        for i in range(n//2):
            nums[i] = 2*(n // 2 - i) + 1
        
        for i in range(n//2, n):
            nums[i] = 2*(i - n // 2);
        
        return nums