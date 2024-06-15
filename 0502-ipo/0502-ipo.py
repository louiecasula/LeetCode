class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Keep a heap for currently affordable projects and another with all zipped vals
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        # Iterate through range of k,
        for i in range(k):
            # While minCapital has elements with capital <= w, pop and push to maxProfit
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)
            # Edgecase: There are no afforable projects
            if not maxProfit:
                break
            # Add popped profit to w
            w += -heapq.heappop(maxProfit)
        # Return w
        return w