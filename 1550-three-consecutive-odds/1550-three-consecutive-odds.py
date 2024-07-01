class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        for a in arr:
            if a % 2 == 1:
                if oddCount == 2:
                    return 1
                oddCount += 1
            else:
                oddCount = 0
        return 0