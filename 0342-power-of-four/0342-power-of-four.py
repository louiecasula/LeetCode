import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            return round(math.log(n, 4), 10) % 1 == 0
        return False