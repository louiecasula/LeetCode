/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    // Keep an output, zCount, and left and right pointers
    let out = 0, zCount = 0, l = 0;
    // Slide da window
    for (let r = 0; r < nums.length; r++) {
        // If right element is 0, increment zCount
        if (nums[r] == 0) { zCount++; }
        // If zCount > k, shift left until it's a zero, decrement zCount
        while (zCount > k) {
            if (nums[l] == 0) { zCount--; }
            l++;
        }
        // If window > output, update output
        out = Math.max(out, r - l + 1);
    }
    // Return output
    return out;
};