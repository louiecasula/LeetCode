class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Keep track of the number of Rs and Ds in senate
        r = senate.count("R")
        d = senate.count("D")
        # Turn senate into a deque
        de = deque(senate)
        # While there are more than 0 of either Rs or Ds,
        while r > 0 and d > 0:
            # Remove the first instance of the opposite char of left-popped char and decrement from count
            curr = de.popleft()
            if curr == "R":
                de.remove("D")
                d -= 1
            else:
                de.remove("R")
                r -= 1
            # Add left-popped char to end of deque
            de.append(curr)
        # If R remains, return Radiant, else return Dire
        if r > 0:
            return "Radiant"
        return "Dire"