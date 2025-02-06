class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        // Keep a counter int and an array of 2 char arrays
        int cnt = 0;
        char[][] diff = new char[][] {{'a', 'a'}, {'a', 'a'}};
        // Iterate length of strings,
        for (int i = 0; i < s1.length(); i++) {
            // If current chars don't equal eachother, increment counter
            if (s1.charAt(i) != s2.charAt(i)) { 
                cnt++;
                // If counter > 2, return false
                if (cnt > 2) { return false; }
                // Update char array differential
                diff[cnt - 1][0] = s1.charAt(i);
                diff[cnt - 1][1] = s2.charAt(i);
            }
        }
        // Return true if counter isn't 1 or if counter isn't 2 and differential arrays aren't opposite chars
        if (cnt == 1 || (cnt == 2 && (diff[0][0] != diff[1][1] || diff[0][1] != diff[1][0]))) { return false; }
        return true;
    }
}