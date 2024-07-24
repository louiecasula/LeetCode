# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edgecase: empty tree
        if not root:
            return None
        # Traverse tree,
        frontier = [root]
        while frontier:
            # Swap left and right
            node = frontier.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                frontier.append(node.left)
            if node.right:
                frontier.append(node.right)
        # Return root
        return root