class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative nums into their own lists (preserving order)
        pos = []
        neg = []
        for num in nums:
            if num >= 0:
                pos.append(num)
            else: neg.append(num)
        # Merge lists together
        ans = []
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
        