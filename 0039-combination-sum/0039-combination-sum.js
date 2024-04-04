/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    // Keep an output array, sort candidates
    let out = [];
    candidates.sort((a, b) => a - b);
    // Make a backtrack function that tests all possible solutions
    var backtrack = function(start, currArr, currSum) {
        // Base case: current array sums to target
        if (currSum === target) {
            out.push([...currArr]);
            return;
        }
        // Iterate nums in input, recursively running function with each num added to current array
        for (let i = start; i < candidates.length; i++) {
            if (currSum + candidates[i] <= target) {
                currArr.push(candidates[i]);
                backtrack(i, currArr, currSum + candidates[i]);
                currArr.pop();
            } else { return; }
        }
    }
    // Run backtrack function and return output
    backtrack(0, [], 0);
    return out;
};