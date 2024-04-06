/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    // Keep an output string and a stack
    let out = "", stack = [];
    // Iterate forwards
    for (let i = 0; i < s.length; i++) {
        // If thesis and top of stack isn't paren, continue
        if (s[i] === ")" && stack.pop() !== "(") { 
            continue;
        } 
        // If element is paren, add to stack
        if (s[i] === "(") { 
            stack.push(s[i]);
        }
        // Append paren or character to output string
        out += s[i];
    }
    // Iterate backwards
    s = "", stack = [];
    for (let i = out.length - 1; i >= 0; i--) {
        // Same logic but excluding extra parens
        if (out[i] === "(" && stack.pop() !== ")") { 
            continue;
        }
        if (out[i] === ")") { 
            stack.push(out[i]);
        }
        s += out[i];
    }
    // Return output string
    return s.split("").reverse().join("");
};