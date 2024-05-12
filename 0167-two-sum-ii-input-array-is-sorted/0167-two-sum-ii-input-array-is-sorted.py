class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Keep a left and right pointer starting at the beginning and end of numbers
        l, r = 0, len(numbers) - 1
        # While left is less than right,
        while l < r:
            # If sum of left and right nums is less than target, increment left
            if numbers[l] + numbers[r] < target:
                l += 1
            # If sum of left and right nums is more than target, decrement right
            elif numbers[l] + numbers[r] > target:
                r -= 1
            # If sum of left and right nums is equal to target, return indices
            else:
                return [l + 1, r + 1]