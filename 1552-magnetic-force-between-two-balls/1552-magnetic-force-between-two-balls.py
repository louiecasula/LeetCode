class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort position array
        position = sorted(position)
        # Helper function to check if m balls is possible in given range
        def good(x):
            start = -sys.maxsize - 1
            count = 0
            for p in position:
                if p - start >= x:
                    start = p
                    count += 1
            return count >= m
        # Use binary search, adjusting low and high depending on helper function result
        low, high = 0, position[-1]
        while low < high:
            mid = (low + high) // 2
            if good(mid + 1):
                low = mid + 1
            else:
                high = mid
        # Return maxDist
        return low