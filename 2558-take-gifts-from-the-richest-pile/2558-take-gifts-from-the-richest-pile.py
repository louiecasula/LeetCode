class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Make gifts a heap
        gifts = [-x for x in gifts]
        heapify(gifts)
        # Iterate to k,
        while k > 0:
            # Pop from heap
            largest = -heappop(gifts)
            # Push floor sqrt of popped element
            heappush(gifts, -isqrt(largest))
            k -= 1
        # Return sum of gifts
        return -sum(gifts)