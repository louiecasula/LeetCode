class Solution {
    public int maxAscendingSum(int[] nums) {
        // Keep an output and running sum int
        int out = nums[0], run = nums[0];
        // Iterate nums to penultimate,
        for (int i = 0; i < nums.length - 1; i++) {
            // If current num < next num, increment run by next and update output if run is larger
            if (nums[i] < nums[i + 1]) { 
                run += nums[i + 1];
                out = Math.max(out, run);
            }
            // Else, set run to 0
            else { run = nums[i + 1]; }
        }
        // Return output
        return out;
    }
}