# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edgecase: linked list is less than two nodes
        if not head or not head.next:
            return head
        # Keep a dummy, odd, and even node and an index
        dummy = ListNode(0)
        odd = dummy
        even = ListNode(0)
        joint = even
        i = 1
        # Traverse linked list
        while head:
            # If i is odd, set odd.next to current node and set odd to odd.next
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            # Else, set even.next to current node and set even to even.next
            else:
                even.next = head
                even = even.next
            # Increment i and move to next node
            head = head.next
            i += 1
        # Set odd.next to joint
        even.next = None
        odd.next = joint.next
        # Return dummy node
        return dummy.next