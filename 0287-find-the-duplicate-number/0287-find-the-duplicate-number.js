/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    // Sort nums
    nums = nums.sort();
    // Iterate until a num repeats
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            return nums[i];
        }
    }
};