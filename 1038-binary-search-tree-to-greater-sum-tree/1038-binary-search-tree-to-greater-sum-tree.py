# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Traverse nodes in descending order, saving them in a list
        nodes = []
        def nodeCatcher(node):
            if node:
                nodeCatcher(node.right)
                nodes.append(node)
                nodeCatcher(node.left)
        nodeCatcher(root)
        # Keep a running sum
        greatCount = 0
        # Iterate node list, add running sum to val
        for node in nodes:
            temp = node.val
            node.val += greatCount
            greatCount += temp
        # Return root
        return root