class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Make a set of one of the lists, check if each num is in the other
        return [x for x in set(nums1) if x in nums2]