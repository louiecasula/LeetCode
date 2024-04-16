# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Edgecase: depth == 1
        if depth == 1:
            dummy = TreeNode(val)
            dummy.left = root
            return dummy
        # Keep a copy of the root
        dummy = root
        # Function to traverse tree up to depth, insert node, and replace existing nodes
        def dfs(root, currDepth):
            # Base case: depth has been reached
            if currDepth == depth - 1:
                tempL, tempR = root.left, root.right
                root.left, root.right = TreeNode(val), TreeNode(val)
                root.left.left, root.right.right = tempL, tempR
            # Recursive case: continue traversing
            if root.left:
                dfs(root.left, currDepth + 1)
            if root.right:
                dfs(root.right, currDepth + 1)
        # Return dummy after dfs function
        dfs(root, 1)
        return dummy