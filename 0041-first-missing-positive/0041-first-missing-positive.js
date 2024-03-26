/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    //// The Constant-Space, Negative Marking Solution ////
    // Replace all nums less than 1 and greater than n with n + 1
    for (let i = 0; i < nums.length; i++) { // Try this with map
        if (nums[i] < 1 || nums[i] > nums.length) {
            nums[i] = nums.length + 1;
        }
    }
    // Iterate again, mark the num at the index of the current num as negative
    for (let i = 0; i < nums.length; i++) { 
        let num = Math.abs(nums[i]);
        if (num > nums.length) {
            continue;
        }
        num--;
        if (nums[num] > 0) {
            nums[num] *= -1;
        } 
    }
    // Iterate again again, if a num is positive, return it
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] >= 0) {
            return i + 1;
        }
    }
    // Return n + 1
    return nums.length + 1
};