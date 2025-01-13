class Solution {
    public int minimumLength(String s) {
        // Keep an output variable
        int out = 0;
        // Map frequency of chars in string
        HashMap<Character, Integer> freq = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) { freq.put(s.charAt(i), freq.getOrDefault(s.charAt(i), 0) + 1); }
        // Iterate keys in map,
        for (char key: freq.keySet()) {
            // If val is even, increment output by 2
            if (freq.get(key) % 2 == 0) { out += 2; }
            // Else, increment output by 1
            else { out++; }
        }
        // Return output
        return out;
    }
}