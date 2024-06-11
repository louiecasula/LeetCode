class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Keep a pointer, l
        N = len(arr1)
        l = 0
        # Iterate length of arr2,
        for num in arr2:
            # Iterate length of output array,
            for r in range(N):
                # If out[j] == arr2[i],
                if arr1[r] == num:
                    # Swap out[l] with out[j] and increment l
                    temp = arr1[l]
                    arr1[l] = arr1[r]
                    arr1[r] = temp
                    l += 1
        # Sort remaining nums after l
        arr1 = arr1[:l] + sorted(arr1[l:])
        # Return arr1
        return arr1