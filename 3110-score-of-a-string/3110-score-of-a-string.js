/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    // Keep an output sum
    let out = 0;
    // Iterate through string, adding the absolute difference between ascii scores to output
    for (let i = 0; i < s.length - 1; i++) {
        out += Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1));
    }
    // Return output
    return out;
};