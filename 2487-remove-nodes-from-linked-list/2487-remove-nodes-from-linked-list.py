# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Keep a list of node vals and two pointer nodes
        vals = deque()
        curr = prev = head
        # Traverse ll, add all vals to list
        while curr:
            vals.append(curr.val)
            curr = curr.next
        curr = prev
        # Iterate queue backwards, save each val as a tuple with the max val so far
        currMax = float(-inf)
        for i in range(len(vals) -1, -1, -1):
            if vals[i] > currMax:
                currMax = vals[i]
            vals[i] = (vals[i], currMax)
        # Traverse ll and queue simultaneously, keep a boolean if head has been established
        isHead = False
        while vals:
            currVal = vals.popleft()
            # If curr val isn't the max val from there on, remove it
            if vals and currVal[0] != currVal[1]:
                prev.next = curr.next
            else:
                if not isHead:
                    head = curr
                    isHead = True
                prev = curr
            curr = curr.next
        # Return head
        return head