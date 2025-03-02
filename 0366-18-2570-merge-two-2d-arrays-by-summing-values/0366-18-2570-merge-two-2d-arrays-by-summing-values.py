class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Keep a map
        nmap = defaultdict(int)
        # Append nums2 to nums1 and sort
        nums = sorted(nums1 + nums2)
        # Iterate nums,
        for num in nums:
            # Add num[1] to map[num[0]]
            nmap[num[0]] += num[1]
        # Return all keys & vals
        return [[k, nmap[k]] for k in nmap]