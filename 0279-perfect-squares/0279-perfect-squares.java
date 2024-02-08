class Solution {
    int count = 0;
    public int numSquares(int n) {
        // Initialize an array of size n + 1, with 0 being the first val, rest being n
        int[] cache = new int[n + 1];
        Arrays.fill(cache, n);
        cache[0] = 0;
        // Iterate from 1 to n
        for (int i = 1; i <= n; i++) {
            // Iterate from 1 to i
            for (int j = 1; j <= i; j++) {
                // j squared = j * j
                int square = j * j;
                // If i - square is less than 0,
                if (i - square < 0) {
                    // Break
                    break;
                }
                // If 1 + cache of (i - square) < cache of i,
                if (1 + cache[i - square] < cache[i]) {
                    // cache of i = 1 + cache of (i - square)
                    cache[i] = 1 + cache[i - square];
                }
            }
        }
        // Return cache of n
        return cache[n];
    }
}