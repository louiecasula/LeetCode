class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Edge case: original isn't compatible with m & n
        if len(original) != m * n:
            return []
        # Keep an output array of m empty arrays and an idx index
        out = [[] for x in range(m)]
        idx = 0
        # Iterate up to m,
        for i in range(m):
            # Iterate up to n,
            for j in range(n):
                # Append ith element to mth output array
                out[i].append(original[idx])
                idx += 1
        # Return output array
        return out