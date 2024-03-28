/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarrayLength = function(nums, k) {
    //// Sliding Window Approach ////
    // Keep a frequency map, max length var, and left and right pointers
    let freq = {}, max = 0, l = 0, r = 0;
    // Iterate until right pointer reaches the end
    while (r < nums.length) {
        // Update freq of each right val
        freq[nums[r]] = nums[r] in freq? freq[nums[r]] + 1: 1;
        // If a val's freq exceeds k, decrement lefts val's freq, shift pointer
        while (freq[nums[r]] > k) {
            freq[nums[l]]--;
            l++;
        }
        // Shift right and update max length
        max = Math.max(max, r - l + 1);
        r++;
    }
    // Return max length
    return max;
};