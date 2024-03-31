/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) {
    // Keep an output and a start, near, far, and right pointers
    let out = 0, s = 0, n = -1, f = -1;
    // Slide through nums
    for (let r = 0; r < nums.length; r++) {
        // If current element outside min and max range, reset pointers and update start
        if (nums[r] > maxK || nums[r] < minK) {
            n = -1;
            f = -1;
            s = r + 1;
        }
        // If current element == minK, update far
        if (nums[r] == minK) { f = r; }
        // If current element == maxK, update near
        if (nums[r] == maxK) { n = r; }
        // Add the window size if positive, else 0
        out += Math.max(0, Math.min(f, n) - s + 1);
    }
    // Return output
    return out;
};