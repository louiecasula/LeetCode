class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Keep an output counter
        out = 0
        # While tickets[k] > 0,
        while tickets[k] > 0:
            # Iterate tickets
            for i in range(len(tickets)):
                # If ticket[k] is 0, break loop
                if tickets[k] == 0:
                    break
                # If element != 0, decrement value, increment output
                if tickets[i] != 0:
                    tickets[i] -= 1
                    out += 1
        # Return output
        return out