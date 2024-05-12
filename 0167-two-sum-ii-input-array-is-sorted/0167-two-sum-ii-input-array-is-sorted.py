class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Keep a left and right pointer starting at the beginning and end of numbers
        l, r = 0, len(numbers) - 1
        # While left is less than right,
        while l < r:
            # Save the sum of left and right nums
            s = numbers[l] + numbers[r]
            # If sum is less than target, increment left
            if s < target:
                l += 1
            # If sum is more than target, decrement right
            elif s > target:
                r -= 1
            # If sum is equal to target, return indices
            else:
                return [l + 1, r + 1]