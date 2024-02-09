class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Make an output list, first diff list, second diff list
        output =[[],[]]
        sn1 = set(nums1)
        sn2 = set(nums2)
        # Iterate first list
        for num in sn1:
            # If not in second list,
            if num not in sn2:
                # Add to fd list
                output[0].append(num)
        # Iterate second list
        for num in sn2:
            # If not in first list,
            if num not in sn1:
                # Add to sd list
                output[1].append(num)
        # Return output
        return output