# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Keep two pointers and a total variable
        l = r = head
        total = 0
        # While r.next isn't null,
        while r:
            # If l isn't pointing at r and r is a 0,
            if l != r and r.val == 0:
                # Set l's next node's val to total, reset total, set l to r
                l.next.val = total
                l.next.next = r.next
                total = 0
                l = r
            # Else,
            else:
                # Increment total by r.val
                total += r.val
            # Shift r pointer
            r = r.next
        # Return head
        return head.next