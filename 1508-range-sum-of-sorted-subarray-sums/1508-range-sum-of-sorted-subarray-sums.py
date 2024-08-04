class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # Make new array of all subarray sums
        MOD = ((10 ** 9) + 7)
        arr = []
        for i in range(n):
            tot = 0
            for j in range(i, n):
                tot += nums[j]
                arr.append(tot)
        # Sort array
        arr.sort()
        # Return sum of all numbers from l -> r
        out = 0
        for i in range(left - 1, right):
            out += arr[i]
        return out % MOD