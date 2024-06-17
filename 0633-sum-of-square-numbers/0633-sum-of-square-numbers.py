class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Keep two pointers at 1 & ~sqrt(c), a & b
        a, b = 0, int(sqrt(c))
        # While a <= b,
        while a <= b:
            squareSum = (a**2) + (b**2)
            # If sum == c, return true
            if squareSum == c:
                return True
            # If sum > c, decrement b
            if squareSum > c:
                b -= 1
            # If sum < c, increment a
            elif squareSum < c:
                a += 1
        # Return false
        return False