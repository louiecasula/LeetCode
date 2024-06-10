class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        return k % ((n - 1) * 2 )if k % ((n - 1) * 2) < n else 2 * n - (k % ((n - 1) * 2)) - 2