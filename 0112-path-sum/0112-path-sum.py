# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Keep an output boolean
        out = False
        # DFS function to sum vals from root to leaf
        def DFS(node, run_sum):
            nonlocal out
            run_sum += node.val
            if not node.left and not node.right and run_sum == targetSum:
                out = True
            if node.left:
                DFS(node.left, run_sum)
            if node.right:
                DFS(node.right, run_sum)
        # Run DFS function and return output
        if root:
            DFS(root, 0)
        return out