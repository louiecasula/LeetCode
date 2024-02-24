class Solution {
    public int removeDuplicates(int[] nums) {
        // Keep a count pointer
        int count = 1;
        // Iterate nums,
        for (int i = 0; i < nums.length - 1; i++) {
            // If current num is equal to next num, continue
            if (nums[i] == nums[i + 1]) { continue; }
            // Else, save current num at the [count] index and increment
            else {
                nums[count] = nums[i + 1];
                count++;
            }
        }
        // Return count
        return count;
    }
}