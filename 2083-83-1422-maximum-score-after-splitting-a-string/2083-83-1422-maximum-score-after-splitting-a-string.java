class Solution {
    public int maxScore(String s) {
        // Count number of 1s
        int count = s.length() - s.replace("1", "").length();
        // Keep an output and a score variable
        int out = 0;
        // Iterate s to penultimate char
        int slen = s.length();
        for (int i = 0; i < slen - 1; i++) {
            // If current char is 0, increment score
            char c = s.charAt(i);
            if (c == '0') { count++; }
            // Else, decrement score
            else { count--; }
            // Update output if score is higher
            out = Math.max(out, count);
        }
        // Return output
        return out;
    }
}