class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Keep a stack and an output array
        out = [-1] * len(nums1)
        stack = []
        # Map each num in nums1 to its index
        map = {n: i for i, n in enumerate(nums1)}
        # Iterate nums2,
        for num in nums2:
            # If current num is greater than top stack val,
            while stack and num > stack[-1]:
                # Set output at index of popped val to current num
                out[map[stack.pop()]] = num
            # If current num is in nums1, add to stack
            if num in nums1:
                stack.append(num)
        # Return output
        return out