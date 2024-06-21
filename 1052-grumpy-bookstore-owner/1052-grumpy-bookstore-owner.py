class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Calculate satisfied customers without using special powers
        out = 0
        N = len(grumpy)
        for i in range(N):
            out = out + customers[i] if grumpy[i] == 0 else out + 0
        # Use minutes a window, slide to end, update output
        for i in range(minutes):
            if grumpy[i] == 1:
                out += customers[i]
        l = 0
        total = out
        while minutes < N:
            if grumpy[minutes] == 1:
                total += customers[minutes]
            if grumpy[l] == 1:
                total -= customers[l]
            out = max(out, total)
            minutes += 1
            l += 1
        # Return output
        return out