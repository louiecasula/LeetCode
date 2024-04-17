# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Keep an output string array
        out = []
        # Function to traverse tree, updating output with smallest lex string
        def dfs(root, string):
            # Base case: End of tree is reached
            if not root.left and not root.right:
                out.append(string)
            # Recursive case: Keep traversing
            if root.left:
                dfs(root.left, chr(root.left.val + 97) + string)
            if root.right:
                dfs(root.right, chr(root.right.val + 97) + string)
        # Run function and return output string.
        dfs(root, chr(root.val + 97))
        out.sort()
        return out[0]