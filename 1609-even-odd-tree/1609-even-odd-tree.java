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
    HashMap<Integer, Stack<Integer>> map = new HashMap();
    boolean even = true;

    public boolean isEvenOddTree(TreeNode root) {
        dfs(root, 0);
        for (Integer key: map.keySet()) {
            if (key % 2 == 0) { even = true; }
            else { even = false; }
            int current = map.get(key).pop();
            if ((even && current % 2 == 0) || (!even && current % 2 == 1)) { return false; }
            while (map.get(key).size() > 0) {
                if ((even && current % 2 == 0) || (!even && current % 2 == 1)) { return false; }
                int next = map.get(key).pop();
                if ((even && next >= current) || (!even && next <= current)) { return false; }
                current = next;
            }
        }
        return true;
    }

    public void dfs(TreeNode root, int depth) {
        if (root == null) { return; }

        if (map.get(depth) == null) {
            map.put(depth, new Stack<Integer>());
        } map.get(depth).push(root.val); 
        

        dfs(root.left, depth + 1);
        dfs(root.right, depth + 1);
    }
}