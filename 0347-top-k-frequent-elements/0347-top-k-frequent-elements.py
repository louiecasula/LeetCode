class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Map frequency of all elements in nums
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # Sort frequency map by values in descending order
        sort = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        # Return slice of frequency map keys up to k
        return list(sort.keys())[:k]