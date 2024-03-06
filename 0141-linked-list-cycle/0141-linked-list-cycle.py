# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edgecase
        if not head:
            return False
        # Iterate
        arch = []
        curr = head
        while curr.next:
            # If map contains node, return false
            if curr in arch:
                return True
            # Save each node
            arch.append(curr)
            curr = curr.next
        # If next node == null, return true
        return False