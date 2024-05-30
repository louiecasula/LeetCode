class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # Keep an output variable
        N = len(arr)
        out = 0
        # Iterate from i = 0 -> length - 1,
        for i in range(N - 1):
            # Initilialize first xor value, a
            a = 0
            # Iterate from j = i + 1 -> length,
            for j in range(i + 1, N):
                # Update a and initialize second xor value, b
                a ^= arr[j - 1]
                b = 0
                # Iterate from k -> length,
                for k in range(j, N):
                    # Update b
                    b ^= arr[k]
                    # If a == b, increment output
                    if a == b:
                        out += 1
        # Return output
        return out