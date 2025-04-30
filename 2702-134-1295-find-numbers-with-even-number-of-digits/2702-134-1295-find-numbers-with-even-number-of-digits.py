class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Keep a even boolean and an output variable
        out = 0
        # Iterate nums,
        for num in nums:
            # Set even to true
            even = True
            # While num > 9,
            while num > 9:
                # Divide it by 10 and flip even val
                num = num // 10
                even = not even
            # If even, increment output
            even = not even
            if even:
                out += 1
        # Return output
        return out