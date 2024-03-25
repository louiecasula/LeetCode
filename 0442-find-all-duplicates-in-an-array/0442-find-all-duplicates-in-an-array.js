/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    //// Sort-of-like-a-linked-list Approach ////
    //// AKA, Flag nums with negative sign ////
    // Keep an output array
    let out = [];
    // Iterate nums, turn that value at the current index's value negative
    for (let i = 0; i < nums.length; i++) {
        // If already negative, add current value to output
        if (nums[Math.abs(nums[i]) - 1] < 0) {
            out.push(Math.abs(nums[i]));
        } else {
            nums[Math.abs(nums[i]) - 1] *= -1;
        }
    }
    // Return output
    return out;
};