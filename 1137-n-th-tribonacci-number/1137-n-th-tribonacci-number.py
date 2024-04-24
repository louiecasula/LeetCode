class Solution:
    def tribonacci(self, n: int) -> int:
        # Edgecase: n is 0, 1, or 2
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # Memoize results
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 1
        # Iterate from 3 to n,
        for i in range(3, n + 1):
            memo[i] = memo[i - 3] + memo[i - 2] + memo[i - 1]
        # Return the nth memo element
        return memo[n]