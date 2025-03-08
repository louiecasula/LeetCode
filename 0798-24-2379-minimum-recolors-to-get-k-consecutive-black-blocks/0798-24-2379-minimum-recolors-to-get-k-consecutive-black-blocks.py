class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Keep a left pointer, a count and output variable
        n = len(blocks)
        l, count, out = 0, 0, n
        # Iterate blocks,
        for r in range(n):
            # If r is white, increment count
            if blocks[r] == "W":
                count += 1
            # If r - l == k:
            if r - l + 1 == k:
                # If count < output, update output
                out = min(out, count)
                # If l is white, decrement count
                if blocks[l] == "W":
                    count -= 1
                # Increment l
                l += 1
        # Return output
        return out