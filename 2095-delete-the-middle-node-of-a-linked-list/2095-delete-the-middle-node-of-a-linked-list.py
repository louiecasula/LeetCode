# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edgecase: there's only one node
        if not head.next:
            return None
        # Keep a dummy node, and a fast and slow pointer
        dummy = slow = head
        fast = head.next
        # Traverse ll until fast reaches the end
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        # Set slow's next to two nodes ahead
        slow.next = slow.next.next
        # Return dummy node
        return dummy