class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Iterate numbers
        n = len(numbers)
        while numbers:
            # If list contains negative (current num - target), return the indexes of both
            curr = numbers.pop()
            needed = -(curr - target)
            if needed in numbers:
                return(numbers.index(needed) + 1, n - (n - len(numbers)) + 1)