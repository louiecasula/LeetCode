class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Map frequency of each num in nums keeping track of the highest frequency
        map = {}
        max = 1
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
                if map[num] > max:
                    max = map[num]
        # Iterate map, if freq == max, add max to output
        out = 0
        for num in map:
            if map[num] == max:
                out += max
        return out