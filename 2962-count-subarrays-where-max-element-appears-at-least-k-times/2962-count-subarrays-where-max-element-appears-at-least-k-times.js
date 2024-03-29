/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k) {
    //// Sliding Window Approach ////
    // Keep an output variable, max value, left and right pointers
    let out = 0, total = 0, max = Math.max(...nums), l = 0, r = 0;
    // Calculate total number of subarrays
    for (let i = 1; i <= nums.length; i++) {
        total += i;
    }
    let max_count = 0;
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