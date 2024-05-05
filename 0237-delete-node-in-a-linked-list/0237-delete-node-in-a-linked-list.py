# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Traverse ll,
        while node:
            # Set node's val to next's val
            node.val = node.next.val
            # If next next node is null, set next to null
            if not node.next.next:
                node.next = None
            # Else, move to next node
            node = node.next