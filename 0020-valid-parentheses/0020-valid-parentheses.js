/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // Keep a stack and a map of parentheses
    let stack = [];
    let map = new Map([[")", "("], ["]", "["], ["}", "{"]]);
    // Iterate through string
    for (let i = 0; i < s.length; i++) {
        // If current element is an open bracket, push to stack
        if (Array.from(map.values()).includes(s[i])) { stack.push(s[i]); }
        // If current element is a closed bracket, and popped element isn't an open bracket, return false
        else if (stack.pop() !== map.get(s[i])) { return false; }
    }
    // If anything is left in the stack, return false
    if (stack.length > 0) { return false; }
    // Return true
    return true;
};