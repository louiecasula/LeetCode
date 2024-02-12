class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # base = x
        # for i in range(abs(n) - 1):
        #     x *= base
        # if n < 0:
        #     return 1 / (x ** n)
        return x ** n