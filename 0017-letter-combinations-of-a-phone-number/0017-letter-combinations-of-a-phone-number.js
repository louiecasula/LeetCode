/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    // Keep an output array and a map of digits to their chars
    let out = [];
    let keyboard = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
                };
    // Make a backtrack function that recursively builds a string based on the input
    var backtrack = function(i, currString) {
        // Once string is built, add it to output
        if (currString.length === digits.length) {
            out.push(currString);
            return;
        }
        // Iterate the current digits' values, recursively incrementing the index and adding to the current string
        Array.from(keyboard[digits[i]]).forEach((c) => backtrack(i + 1, currString + c));
    };
    // Edgecase: input is empty array, return empty array
    if (digits.length > 0) {
        // Call backtrack function with index of 0 and an empty string
        backtrack(0, "");
    }
    return out;
};