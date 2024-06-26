# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodeList = []
        # Function for in-order traversal of bst that returns sorted list of nodes
        def iot(node):
            if node:
                iot(node.left)
                nodeList.append(node)
                iot(node.right)
        # Run iot function
        iot(root)
        # Function to balance bst
        def balance(start, end):
            # Base case: start is greater than end
            if start > end:
                return None
            
            mid = (start + end) // 2
            node = nodeList[mid]
            node.left = balance(start, mid - 1)
            node.right = balance(mid + 1, end)
            return node
        
        # Return result of balance function
        return balance(0, len(nodeList) - 1)