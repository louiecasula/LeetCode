/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    // Keep output and sum variables
    let out = 0, sum = 0;
    // Iterate input
    for (let i = 0; i < s.length; i++) {
        // If current element is opening paren, increment sum
        if (s[i] === "(") { sum++; }
        // If current element is closing paren, decrement sum
        if (s[i] === ")") { sum--; }
        // If sum is > output, update output
        out = Math.max(out, sum);
    }
    // Return output
    return out;
};