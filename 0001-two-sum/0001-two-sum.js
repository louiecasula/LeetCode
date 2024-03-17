/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //// Hash map method ////
    val_map = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (val_map.has(target - nums[i])) {
            return [val_map.get(target - nums[i]), i];
        }
        val_map.set(nums[i], i);
    }
    return -1;
};