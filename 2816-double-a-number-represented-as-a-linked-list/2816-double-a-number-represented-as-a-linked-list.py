# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(100000)

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Keep a dummy node and a num string
        dummy = head
        numString = ""
        # Traverse ll, concat val to string
        while dummy:
            numString += str(dummy.val)
            dummy = dummy.next
        dummy = head
        # Double num string
        doubleNum = deque(str(int(numString) * 2))
        # If there's an extra digit, create new node as new head
        if len(doubleNum) > len(numString):
            dummy = ListNode(val=doubleNum.popleft(), next=head)
            head = dummy
            dummy = dummy.next
        # Traverse ll while iterating num string, set each val to string val
        while dummy:
            dummy.val = doubleNum.popleft()
            dummy = dummy.next
        # Return head
        return head
