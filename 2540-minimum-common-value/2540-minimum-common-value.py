class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Edgecase
        if nums1[len(nums1) - 1] < nums2[0] or nums2[len(nums2) - 1] < nums1[0]:
            return -1
        if len(nums1) < len(nums2):
            for num in nums1:
                if num in nums2:
                    return num
        else:
            for num in nums2:
                if num in nums1:
                    return num
        return -1