/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    // Function that recursively makes string "good"
    var recursion = function(st) {
        // Keep an output string and a flag that changes if string is altered
        let currString = "";
        let flag = true;
        // Iterate, if current's ASCII !== next +- 32, append to output
        for (let i = 0; i < st.length; i++) {
            if (st.charCodeAt(i) === st.charCodeAt(i + 1) + 32 ||
            st.charCodeAt(i) === st.charCodeAt(i + 1) - 32) {
                flag = false;
                i++;
            }
            else {
                currString += st[i];
            }
        }
        // If flag is false, call with resulting string, else return string
        if (flag === true) {
            return currString;
        } else {
            return recursion(currString);
        }
    }
    // Return recursive function's output
    return recursion(s);
};