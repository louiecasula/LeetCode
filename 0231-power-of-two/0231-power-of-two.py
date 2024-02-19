import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Return (log base 2 of n) % 1 == 0
        if n > 0:
            return (math.log2(n)) % 1 == 0
        return False