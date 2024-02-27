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
    private int max;
    
    public int diameterOfBinaryTree(TreeNode root) {
        max = 0;
        dfs(root);
        return max;
    }
    
    public int dfs(TreeNode root) {
        System.out.println(max);
        if (root == null) { return -1; }
        int left = dfs(root.left);
        int right = dfs(root.right);
        max = Math.max(max, (2 + left + right));
        return Math.max(left, right) + 1;
    }
}