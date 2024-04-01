/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    // Split string by spaces
    s = s.split(' ');
    // Filter out any extra spaces
    s = s.filter((a) => a !== '');
    // Return length of final element
    return s[s.length - 1].length;
};