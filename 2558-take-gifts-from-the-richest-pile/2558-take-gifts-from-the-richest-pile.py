class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Iterate to k,
        for i in range(k):
            # Sort gifts
            gifts = sorted(gifts)
            # Change largest gift to floor square root
            gifts[-1] = floor(sqrt(gifts[-1]))
        # Return sum of gifts
        return sum(gifts)