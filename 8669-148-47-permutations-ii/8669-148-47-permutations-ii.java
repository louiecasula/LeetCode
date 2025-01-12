class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        // Keep an output list of lists of integers
        List<List<Integer>> out = new ArrayList<List<Integer>>();
        // Map frequency of nums
        Map<Integer, Integer> freq = new HashMap<Integer, Integer>();
        for (int num: nums) { freq.put(num, freq.getOrDefault(num, 0) + 1); }
        // Run method and return output
        int n = nums.length;
        backtrack(out, new ArrayList<>(), freq, n);
        return out;
    }
    // Method to recursively run all permutations
    public static void backtrack(List<List<Integer>> out, List<Integer> curr, Map<Integer, Integer> freq, int n) {
        // Base case: all numbers are used, append list to output
        if (curr.size() == n) { out.add(new ArrayList<>(curr)); }
        // Recursive case
        // Iterate through keys in freq,
        for (int key: freq.keySet()) {
            // If val is greater than 0, add key to curr, run backtrack, remove key from curr
            if (freq.get(key) > 0) {
                curr.add(key);
                freq.put(key, freq.get(key) - 1);
                backtrack(out, curr, freq, n);
                curr.remove(curr.size() - 1);
                freq.put(key, freq.get(key) + 1);
            }
        }
    }
}