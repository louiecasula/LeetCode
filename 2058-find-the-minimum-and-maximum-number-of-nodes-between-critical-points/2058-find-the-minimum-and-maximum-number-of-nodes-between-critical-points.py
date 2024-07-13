# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Keep an array of critical indexes, min dist, and max dist variables
        crit = []
        minDist, maxDist = sys.maxsize, -1
        i = 0
        prev = head.val
        # Traverse nodes,
        while head.next != None:
            # If node val is greater or less than surrounding vals, add index to array
            if i != 0 and ((prev < head.val > head.next.val) or (prev > head.val < head.next.val)):
                crit.append(i)
            i += 1
            prev = head.val
            head = head.next
        # Edgecase: Return [-1, -1] if array is less than two vals
        N = len(crit)
        print(crit)
        if N < 2:
            return [-1, -1]
        # Iterate array,
        maxDist = crit[-1] - crit[0]
        for i in range(N - 1):
            # Update min dist and max dist
            minDist = min(minDist, crit[i + 1] - crit[i])
        # Return [min dist, max dist]
        return [minDist, maxDist]