/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    //// Constant space, n time Solution ////
    // Keep a leftMin and leftMax counter
    let leftMin = 0, leftMax = 0;
    // Iterate string
    for (let c of s) {
        // If paren, increment both
        if (c === "(") {
            leftMin++;
            leftMax++;
        }
        // Else if thesis, decrement both
        else if (c === ")") {
            leftMin--;
            leftMax--;
        }
        // Else, decrement min, increment max
        else {
            leftMin--;
            leftMax++;
        }
        // If max is negative, return false
        if (leftMax < 0) { return false; }
        // If min is negative, reset to 0
        if (leftMin < 0) { leftMin = 0; }
    }
    // Return true if min is 0
    return leftMin === 0;
};