/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    // Keep left and right pointers
    let l = 0, r = 0;
    // Slide da window
    for (; r < nums.length; r++) {
        // If right element is 0, decrement k
        if (nums[r] == 0) { k--; }
        // If k is negative, shift left, increment k
        if (k < 0) {
            if (nums[l] == 0) { k++; }
            l++;
        }
    }
    // Return window size
    return r - l;
};