# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    # DFS approach to find leaf nodes
        # Base case: end of tree reached
        if not root:
            return None
        # Recursive case: post-order DFS
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        # If leaf node's val == target, delete
        if not root.left and not root.right and root.val == target:
            return None
        # Else, return root
        return root