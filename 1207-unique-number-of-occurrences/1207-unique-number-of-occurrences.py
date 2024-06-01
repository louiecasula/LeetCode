class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Make a counter
        c = Counter(arr)
        # Return length of set of counter values == length of counter keys
        return len(set(c.values())) == len(c.keys())