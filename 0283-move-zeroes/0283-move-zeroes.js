/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    //// Two pointers Approach ////
    // Keep a counter for non zeroes
    let zero = 0;
    // Iterate
    for (let i = 0; i < nums.length; i++) {
        // If current element is non zero, change element at index of counter to current, increment counter
        if (nums[i] !== 0) {
            nums[zero] = nums[i];
            zero++;
        }
    }
    // Fill in the rest of the array from counter + 1 to end of array with zeroes
    for (; zero < nums.length; zero++) {
        nums[zero] = 0;
    }
    // Return nums
    return nums;
};