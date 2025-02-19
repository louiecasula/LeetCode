# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find length of linked list
        dummy = head
        n = 0
        while dummy:
            n += 1
            dummy = dummy.next
        # Split linked list into two halves
        half = head
        for i in range((n // 2) - 1):
            half = half.next
        dummy = half.next
        half.next = None
        # Reverse second half of linked list
        tail = prev = dummy
        if not dummy.next:
            return dummy.val + head.val
        dummy = dummy.next
        tail.next = None
        while dummy.next:
            prev = dummy
            dummy = dummy.next
            prev.next = tail
            tail = prev
        dummy.next = prev
        # Keep an output and a running sum variable
        out = csum = 0
        # Traverse both halves,
        while dummy:
            # Update output if running sum is greater
            out = max(out, head.val + dummy.val)
            head = head.next
            dummy = dummy.next
        # Return output
        return out