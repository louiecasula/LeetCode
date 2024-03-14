/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var numSubarraysWithSum = function(nums, goal) {
    let out = 0;
    if (nums.length > 1) {
        // For loop
        for (let i = 0; i < nums.length - 1; i++) {
            let sum = nums[i];
            if (sum > goal) { continue; }
            if (sum == goal) { out++; }
            // Nested for loop
            for (let j = i + 1; j < nums.length; j++) {
                sum += nums[j];
                if (sum > goal) { break; }
                if (sum == goal) { out++; }
            }
        }
    }
    if (nums[nums.length - 1] == goal) { out++; }
    // Return out
    return out;
};