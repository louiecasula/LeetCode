class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Keep an output array
        out = []
        # Map frequency of all elements in nums
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # In the range of k, add max frequency num, then remove it from map
        while k > 0:
            top = (0, 0)
            for x in freq.items():
                if x[1] > top[1]:
                    top = x
            out.append(top[0])
            del freq[top[0]]
            k -= 1
        # Return output
        return out