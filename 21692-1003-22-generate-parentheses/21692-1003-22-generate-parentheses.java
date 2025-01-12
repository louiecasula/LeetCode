class Solution {
    public List<String> generateParenthesis(int n) {
        // Keep an output list
        ArrayList<String> out = new ArrayList<String>();
        // Run backtracking method and return output
        backtrack(out, new StringBuilder(), n, 0, 0);
        return out;
    }
    // Method to run all combos
    public void backtrack(ArrayList<String> out, StringBuilder temp, int n, int lp, int rp) {
        // Base case: n sets of parentheses are used
        if (temp.length() == 2 * n) { out.add(temp.toString()); }
        // Recursive case: keep making combos
        // If lp less than n, append paren to temp, run backtrack, remove paren
        if (lp < n) {
            temp.append("(");
            backtrack(out, temp, n, lp + 1, rp);
            temp.deleteCharAt(temp.length() - 1);
        }
        // If rp less than lp, append thesis to temp, run backtrack, remove thesis
        if (rp < lp) {
            temp.append(")");
            backtrack(out, temp, n, lp, rp + 1);
            temp.deleteCharAt(temp.length() - 1);
        }
    }
}