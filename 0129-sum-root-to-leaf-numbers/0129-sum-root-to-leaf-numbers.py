# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS function that adds each root-to-leaf number to eachother
        def dfs(root, curr):
            # Base case: root is null
            if not root:
                return 0
            # Update current number with new node value
            curr = curr * 10 + root.val
            # Return number once a leaf node is reached
            if not root.left and not root.right:
                return curr
            # Recursively call dfs with updated number
            return dfs(root.left, curr) + dfs(root.right, curr)
        # Return result of dfs
        return dfs(root, 0)