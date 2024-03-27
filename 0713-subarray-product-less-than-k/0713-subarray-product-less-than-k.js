/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    //// Sliding Window Approach ////
    // Edgecase
    if (k <= 1) { return 0; }
    // Iterate nums with left and right pointers updating running product
    let left = 0, right = 0, prod = 1, out = 0;
    while (right < nums.length) {
        prod *= nums[right];
        // If product is greater than k, divide by left val, shift left pointer
        while (prod >= k) {
            prod /= nums[left];
            left++;
        }
        out += right - left + 1;
        right++;
    }
    // Return output
    return out;
};