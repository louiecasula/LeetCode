/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    // Backtrack function that builds string by traversing 2D array
    var backtrack = function(i, j, string, visited) {
        // Base case: string is equal to word
        if (string === word) {
            return true;
        }
        // Base case: index is out of bounds or already visited
        if (i < 0 || i >= board.length ||
            j < 0 || j >= board[0].length ||
            visited.includes(`${i},${j}`)) {
            return false;
        }
        // If current cell === current letter in word, call backtrack on surrounding cells, return true if any of them returns true
        if (board[i][j] === word[string.length]) {
            string += board[i][j];
            let v = [...visited, `${i},${j}`];
            if (backtrack(i + 1, j, string, v) || backtrack(i - 1, j, string, v) ||
                backtrack(i, j + 1, string, v) || backtrack(i, j - 1, string, v)) {
                return true;
            }
        }
    };
    // Iterate column
    for (let i = 0; i < board.length; i++) {
        // Iterate row
        for (let j = 0; j < board[0].length; j++) {
            // If current element == first letter of word,
            if (board[i][j] == word[0]) {
                // If backtrack function is true,
                if (backtrack(i, j, "", []) === true) {
                    // Return true
                    return true;
                }
            }
        }
    }
    // Return false
    return false;
};