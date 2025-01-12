class Solution {

    public List<List<Integer>> permute(int[] nums) {
        // Keep an output list of lists of integers
        List<List<Integer>> out = new ArrayList<List<Integer>>();
        // Run method and return output
        backtrack(out, new ArrayList<>(), nums);
        return out;
    }

    // Method to recursively run all permutations
    public static void backtrack(List<List<Integer>> out, List<Integer> curr, int[] nums) {
        // Base case: all numbers are used, append list to output
        if (curr.size() == nums.length) { out.add(new ArrayList<>(curr)); }
        // Recursive case
        // Iterate through nums
        for (int i = 0; i < nums.length; i++) {
            // If curr doesn't contain nums[i], add it, call method, remove it
            if (!curr.contains(nums[i])) {
                curr.add(nums[i]);
                backtrack(out, curr, nums);
                curr.remove(curr.size() - 1);
            }
        }
    }
}