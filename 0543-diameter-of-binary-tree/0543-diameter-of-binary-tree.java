/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private static int max = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        int out = max;
        max = 0;
        return out;
    }
    
    public int dfs(TreeNode root) {
        System.out.println(max);
        if (root == null) { return -1; }
        int left = dfs(root.left);
        int right = dfs(root.right);
        if (max < (2 + left + right)) {
            max = (2 + left + right);
        }
        if (left >= right) {
            return 1 + left;
        } return 1 + right;
    }
}