class Solution {
    public String removeOccurrences(String s, String part) {
        // Keep a variable for length of s, n
        int n = s.length();
        s = s.replaceFirst(part, "");
        // While n != length of s,
        while (n != s.length()) {
            // Set n to length of s
            n = s.length();
            // Replace part in s with nothing
            s = s.replaceFirst(part, "");
        }
        // Return s
        return s;
    }
}