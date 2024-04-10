class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck
        deck.sort()
        # Keep an output array and a queue from 0 to length of deck
        out = [0] * len(deck)
        q = [x for x in range(len(deck))]
        # Iterate deck
        for c in deck:
            # Make the output's element at the index of left-popped q = current deck element
            i = q.pop(0)
            out[i] = c
            # Shift the next left-popped q element to the end of the q
            if q:
                q.append(q.pop(0))
        # Return output
        return out