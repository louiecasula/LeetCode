# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: end of ll is reached
        if head is None or head.next is None:
            return head
        # Recursive case: continue traversing ll
        remaining = self.removeNodes(head.next)
        # If current val is less than remaining, skip (return remaining)
        if head.val < remaining.val:
            return remaining
        # Else, link nodes
        head.next = remaining
        return head