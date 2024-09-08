class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Frequency map
        # Map each element by its frequency
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # Add each value & key in a tuple
        tupList = [(val, key) for key, val in freq.items()]
        # Sort tuple list
        tupList.sort(reverse=True)
        # Return k keys from tuple list
        return [x[1] for x in tupList[0:k]]