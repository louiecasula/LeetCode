class Solution:
    def mincostToHireWorkers(self, quality: List[int], min_wage: List[int], k: int) -> float:
        # Make a ratio array populated by tuples of min_wage/quality, quality
        ratio = sorted([(w / q, q) for w, q in zip(min_wage, quality)])
        # Keep a priority queue, quality sum counter, and maximum ratio
        max_heap = []
        quality_sum = 0
        max_ratio = 0.0
        # For each ratio,
        for i in range(k):
            # Update maximum ratio, add to quality sum, and push quality to pq
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])
        # Keep an output variable set to the maximum ratio * sum of quality values
        cost = max_ratio * quality_sum
        # For each worker with a viable ratio,
        for i in range(k, len(quality)):
            # Check for smaller total cost
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -ratio[i][1])
            cost = min(cost, max_ratio * quality_sum)
        # Return output
        return cost