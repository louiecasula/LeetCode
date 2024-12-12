class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Iterate to k,
        for i in range(k):
            # Find largest gift
            largest = max(gifts)
            # Change largest gift to floor square root
            gifts[gifts.index(largest)] = floor(sqrt(largest))
        # Return sum of gifts
        return sum(gifts)