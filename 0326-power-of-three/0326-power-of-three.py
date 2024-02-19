import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            return round(math.log(n, 3), 10) % 1 == 0
        return False