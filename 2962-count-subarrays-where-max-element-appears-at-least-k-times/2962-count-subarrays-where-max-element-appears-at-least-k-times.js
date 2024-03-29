/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k) {
    //// Sliding Window Approach ////
    // Keep an output variable, max value, max count, left and right pointers
    let out = 0, max = Math.max(...nums), max_count = 0, l = 0;
    // Iterate until right reaches the end of array
    for (let r = 0; r < nums.length; r++) {
        if (nums[r] == max) { max_count++; }
        // If max_count == k, shift left until it doesn't
        while (max_count == k) {
            if (nums[l] == max || nums[l] == nums[r]) { max_count--; }
            l++;
        }
        // Add window size to output
        out += r - l + 1;
    }
    // Return total subarrays - output
    return ((nums.length * (nums.length + 1)) / 2) - out;
};