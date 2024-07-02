class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Determine the smaller of the arrays and keep frequency map for larger
        smaller, larger = nums1, nums2
        if nums1 > nums2:
            smaller, larger = nums2, nums1
        freq = defaultdict(int)
        for num in larger:
            freq[num] += 1
        # Keep an output array
        out = []
        # Iterate smaller array,
        for num in smaller:
            # If it's in larger map,
            if num in freq and freq[num] > 0:
                # Append to output and decrement map value
                out.append(num)
                freq[num] -= 1
        # Return output
        return out