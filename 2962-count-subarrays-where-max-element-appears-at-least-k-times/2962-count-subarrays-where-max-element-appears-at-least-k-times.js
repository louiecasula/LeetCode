/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k) {
    //// Sliding Window Approach ////
    // Keep an output variable, max value, max count, left and right pointers
    let out = 0, max = Math.max(...nums), max_count = 0, l = 0, r = 0;
    // Calculate total number of subarrays
    let total = (nums.length * (nums.length + 1)) / 2;
    // Iterate until right reaches the end of array
    while (r < nums.length) {
        if (nums[r] == max) { max_count++; }
        // If max_count == k, shift left until it doesn't
        while (max_count == k) {
            if (nums[l] == max || nums[l] == nums[r]) { max_count--; }
            l++;
        }
        // Else, add window size to output
        out += r - l + 1;
        r++;
    }
    // Return total - output
    return total - out;
};