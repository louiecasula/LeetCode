class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        # Map elements,
        for num in nums:
            print(num)
            if num in freq:
                freq[num] += 1
            if num not in freq:
                freq[num] = 1
            # If the value of the current key > n / 2
            if freq[num] > len(nums) / 2:
                # Return element
                return num