# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Keep an output variable
        out = 0
        # Use DFS to reach leaf nodes
        def dfs(node):
            nonlocal out
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            out += abs(left) + abs(right)
            return node.val + left + right - 1
        # Run dfs on root node and return output
        dfs(root)
        return out