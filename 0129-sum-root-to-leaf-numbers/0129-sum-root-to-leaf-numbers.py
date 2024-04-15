# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Keep a list of root-to-leaf numbers
        rtl = []
        # DFS function that adds each root-to-leaf number to a list
        def dfs(root, numString):
            if root.left:
                dfs(root.left, numString + str(root.left.val))
            if root.right:
                dfs(root.right, numString + str(root.right.val))
            if not root.left and not root.right:
                rtl.append(int(numString))
        
        dfs(root, str(root.val))
        return sum(rtl)