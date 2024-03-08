class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Map frequency of each num in nums keeping track of the highest frequency
        map = {}
        max = 1
        out = 0
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
            if map[num] > max:
                max = map[num]
                out = max
                continue
            if map[num] == max:
                out += max
        # Iterate map, if freq == max, add max to output
        return out