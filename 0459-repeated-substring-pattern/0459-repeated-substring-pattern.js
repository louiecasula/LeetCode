/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function(s) {
    // Iterate half the length of string,
    for (let i = 0; i < Math.floor(s.length / 2); i++) {
        // If length is divisible by substring length,
        if (s.length % (i + 1) == 0) {
            // Concatenate substring together until its length equals string's length
            let sub = s.slice(0, i + 1);
            let comp = "";
            while (comp.length !== s.length) { comp += sub; }
            // If the strings are the same, return true
            if (comp === s) { return true; }
        }
    }
    // Return false
    return false;
};