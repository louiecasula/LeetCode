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
    var backtrack = function(currArr, currSum) {
        // Base case: current array sums to target
        if (currSum === target) {
            // Check if current array is already in output array
            currArr.sort((a, b) => a - b);
            for (let i = 0; i < out.length; i++) {
                if (JSON.stringify(out[i]) === JSON.stringify(currArr)) {
                    return;
                }
            }
            out.push(currArr);
            return;
        }
        // Iterate nums in input, recursively running function with each num added to current array
        for (let i = 0; i < candidates.length; i++) {
            if (currSum + candidates[i] <= target) {
                backtrack([...currArr, candidates[i]], currSum + candidates[i]);
            } else { return; }
        }
    }
    // Run backtrack function and return output
    backtrack([], 0);
    return out;
};