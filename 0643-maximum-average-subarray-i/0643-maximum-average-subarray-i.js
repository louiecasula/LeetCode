/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    // Keep an output and a running sum
    let sum = 0;
    // Get the sum up to kth element
    for (let i = 0; i < k; i++) {
        sum += nums[i];
    }
    let out = sum / k;
    // Iterate from k onwards, adding and subtracting elements from sum as they enter and exit the window, set the output to the higher of current output and new average
    for (let i = k; i < nums.length; i++) {
        sum = sum - nums[i - k] + nums[i];
        out = Math.max(out, sum / k);
    }
    // Return output
    return out;
};