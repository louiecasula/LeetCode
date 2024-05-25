class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Keep an output array set to zeroes and a stack
        N = len(temperatures)
        out = [0] * N
        stack = []
        # Iterate temperatures,
        for i in range(N):
            # While current temp is greater than top of stack,
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                # Set output to difference in index of popped temp - index of current temp
                popped = stack.pop()
                out[popped[1]] = i - popped[1]
            # Add current temp to stack
            stack.append((curr, i))
        # Return output
        return out