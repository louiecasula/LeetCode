class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Keep an output variable and two pointers
        out = 0
        w = p = 0
        # Zip profit and difficulty, sort by profit; sort profit & worker
        proDif = list(sorted(zip(profit, difficulty), reverse=True))
        worker = sorted(worker, reverse=True)
        # Walk w and p pointers,
        while w < len(worker) and p < len(proDif):
            # If difficulty[p] <= worker[w], increment output and w
            if proDif[p][1] <= worker[w]:
                out += proDif[p][0]
                w += 1
            # Else, increment p
            else:
                p += 1
        # Return output
        return out