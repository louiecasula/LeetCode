# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Keep an output sum variable
    out = 0
    # Recursively traverse tree, adding all left nodes to output
    def traverse(self, root):
        if root.left:
            if not root.left.left and not root.left.right:
                self.out += root.left.val
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)
            
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Run recursive function
        self.traverse(root)
        # Return output
        return self.out