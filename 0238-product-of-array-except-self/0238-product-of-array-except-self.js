/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    //// Prefix, Postfix method ////
    // Make an output array
    out = [];
    // Iterate forward, saving the running product at each index
    prefix = 1;
    for (let i = 0; i < nums.length; i++) {
        out[i] = prefix;
        prefix *= nums[i];
    }
    // Iterate backwards, saving the running product * current output value
    postfix = 1;
    for (let i = nums.length -1; i >= 0; i--) {
        out[i] *= postfix;
        postfix *= nums[i];
    }
    // Return output
    return out;
};