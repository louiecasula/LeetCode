# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Keep a max depth variable
        out = 0
        # DFS function to reach the deepest leaf node
        def DFS(node, depth):
            nonlocal out
            out = max(out, depth)
            if node.left:
                DFS(node.left, depth + 1)
            if node.right:
                DFS(node.right, depth + 1)
        # Run DFS function and return output
        if root:
            DFS(root, 1)
        return out