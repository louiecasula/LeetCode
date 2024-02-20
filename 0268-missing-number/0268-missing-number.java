class Solution {
    public int missingNumber(int[] nums) {
        // Sort nums
        Arrays.sort(nums);
        // Iterate
        for (int i = 0; i < nums.length; i++) {
            // If element doesn't equal i,
            if (i != nums[i]) {
                // Return i
                return i;
            }
        }
        // Return length of array
        return nums.length;
    }
}